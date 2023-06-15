# Register your models here.
from django.contrib import admin
from .models import SiteReview, Comments

# Register your models here.


@admin.register(SiteReview)
class SiteReviewAdmin(admin.ModelAdmin):
    list_display = (
        "heading",
        "created_at",
        "author",
        "body",
        "updated_at",
    )
    list_filter = ["author", "heading", "updated_at"]

    ordering = ("-created_at",)


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("user", "review", "body", "created_at", "allowed")
