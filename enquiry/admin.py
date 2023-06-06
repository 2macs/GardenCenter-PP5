from django.contrib import admin


from django.contrib import admin
from .models import MakeEnquiry


@admin.register(MakeEnquiry)
class EnquiryManage(admin.ModelAdmin):
    display_all = ["date_submitted", "name", "heading", "message_body", "acknowledged"]
    list_filter = ["date_submitted", "name", "acknowledged"]
    search_fields = ["name", "heading", "message_body"]
    date_hierarchy = "date_submitted"
