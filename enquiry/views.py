from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import EnquiryForm


def make_enquiry(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            form.save()
            messages.info(
                request, f"Your enquiry has been registered, we will respond asap"
            )
            subject = f"Thank you for your enquiry"
            body = f"Dear {cd['name']} , we will respond asap"
            send_mail(
                subject,
                body,
                "amcneill83@gmail.com",
                [
                    cd["email"],
                ],
                fail_silently=False,
            )
    else:
        form = EnquiryForm()
    return render(request, "enquiry/enquiry.html/", {"form": form})


def subscribe_sign_up(request):
    return render(request, "enquiry/subscribe.html/")
