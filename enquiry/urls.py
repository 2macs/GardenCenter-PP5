from django.urls import path
from . import views

urlpatterns = [
    path("", views.make_enquiry, name="make_enquiry"),
]