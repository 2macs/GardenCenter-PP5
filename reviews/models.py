from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User

# Create your models here.


# Reviews model
class SiteReview(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name = 'site_review')
    heading = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [models.Index(fields=['-created_at']),]

    def __str__(self):
        return self.title


# Comments model
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(
        SiteReview, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    allowed = models.BooleanField(default=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.review.heading}'

