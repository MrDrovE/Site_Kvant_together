from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "view_data_link")
    search_fields = ("name",)
    fields = ['name','mail','join_time']

    def view_data_link(self, obj):
        count = obj.name
        url = (
                reverse("admin:app_user_changelist")
                + "?"
                + urlencode({"category_id": f"{obj.name}"})
        )
        return format_html('<a href = "{}" > {} </a>', url, count)

    view_data_link.short_description = "User_name"

# Register your models here.
