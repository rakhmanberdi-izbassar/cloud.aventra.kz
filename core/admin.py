from django.contrib import admin
from .models import Tour, TourImage
from .models import Location, City

class TourImageInline(admin.TabularInline):
    model = TourImage
    extra = 1

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'user', 'price', 'volume', 'date', 'featured')
    list_filter = ('featured', 'location', 'date')
    search_fields = ('name', 'description')
    inlines = [TourImageInline]

@admin.register(TourImage)
class TourImageAdmin(admin.ModelAdmin):
    list_display = ('tour', 'image_path')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')  # Админкада көрсетілетін бағандар

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'city_code']
    search_fields = ['name', 'city_code']