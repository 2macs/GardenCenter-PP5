from django.urls import path
from . import views

urlpatterns = [
    path("reviews/", views.all_reviews, name="all_reviews"),
    path("create_review/", views.create_review, name="create_review"),
]
