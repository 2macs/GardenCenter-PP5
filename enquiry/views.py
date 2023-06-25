from django.shortcuts import render
from django.contrib import messages

from .forms import EnquiryForm


def make_enquiry(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(
                request, f"Your enquiry has been registered, we will respond asap"
            )
    else:
        form = EnquiryForm()
    return render(request, "enquiry/enquiry.html/", {"form": form})


def subscribe_sign_up(request):
     return render(request, "enquiry/subscribe.html/")

