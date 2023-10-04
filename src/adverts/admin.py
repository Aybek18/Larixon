from django.contrib import admin

from adverts.models import Advert


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    fields = ("id", "created_at", "title", "description", "city", "category", "views",)
    readonly_fields = ("id", "views", "created_at",)
