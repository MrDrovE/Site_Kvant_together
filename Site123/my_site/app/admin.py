from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from .models import Articles
# Register your models here.



@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','meta','date',)

    # def view_data_link(self, obj):
    #     count = obj.user_set.count()
    #     url = (
    #             reverse("admin:app_user_changelist")
    #             + "?"
    #             + urlencode({"category_id": f"{obj.id}"})
    #     )
    #     return format_html('<a href = "{}"> {} </a>', url, count)

    #view_data_link.short_description = "Articles"
