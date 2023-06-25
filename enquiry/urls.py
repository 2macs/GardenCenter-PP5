from django.urls import path
from . import views

urlpatterns = [
    path("", views.make_enquiry, name="make_enquiry"),
    path("subscribe/", views.subscribe_sign_up, name="subscribe_sign_up"),
]
