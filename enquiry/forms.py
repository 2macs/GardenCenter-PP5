from .models import MakeEnquiry
from django import forms


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = MakeEnquiry
        fields = ["name", "email", "heading", "message_body"]
