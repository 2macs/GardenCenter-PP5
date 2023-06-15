from django.shortcuts import render
from .models import SiteReview

# View all site reviews


def all_reviews(request):
    reviews = SiteReview.objects.all()
    return render(request, "reviews/reviews.html", {"reviews": reviews})
