from .models import SiteReview
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = SiteReview
        fields = [
            "heading",
            "body",
        ]
