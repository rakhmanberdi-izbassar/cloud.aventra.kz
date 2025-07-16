from django.contrib import admin
from .models import Hotel, RoomType

class RoomTypeInline(admin.TabularInline):
    model = RoomType
    extra = 1

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'stars', 'price_per_night', 'is_active')
    list_filter = ('city', 'stars', 'is_active')
    search_fields = ('name', 'address', 'city__name')
    inlines = [RoomTypeInline]

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'name', 'price_per_night', 'available_rooms')
    list_filter = ('hotel',)
