from django.urls import path
from . import views

urlpatterns = [
    path("reviews/", views.all_reviews, name="all_reviews"),
    path("create_review/", views.create_review, name="create_review"),
    path("get_user_review/", views.get_user_review, name="get_user_review"),
    path(
        "delete review/<int:user_review_id>/",
        views.delete_review,
        name="delete_review"
    ),
    path(
        "edit review/<int:user_review_id>/",
        views.edit_review,
        name="edit_review"),
    path("add_comment/<int:review_id>/",
         views.add_comment,
         name="add_comment"),
]
