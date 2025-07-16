from django.contrib import admin
from .models import Event, EventType

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'city', 'event_type', 'organizer')
    list_filter = ('city', 'event_type', 'start_date')
    search_fields = ('title', 'description', 'location_name', 'organizer')

@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
