from django.contrib import admin
from .models import Place

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "country")
    search_fields = ("name", "city", "country")
    list_filter = ("country",)