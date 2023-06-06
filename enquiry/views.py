from django.shortcuts import render
from .forms import EnquiryForm

# Create your views here.
# Create your views here.
# Templates are Index, booking,enquire,explore


def make_enquiry(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EnquiryForm()
    return render(request, "enquiry/enquiry.html/", {"form": form})
