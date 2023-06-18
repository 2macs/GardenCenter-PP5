from .models import SiteReview, Comments
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = SiteReview
        fields = [
            "heading",
            "body",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            "user",
            "review",
            "body",
        ]
