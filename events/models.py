# events/models.py
from django.db import models
from django.contrib.auth import get_user_model
from core.models import City

User = get_user_model()

class EventType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    event_type = models.ForeignKey(EventType, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    location_name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    price_info = models.CharField(max_length=255, blank=True)
    organizer = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    image = models.ImageField(upload_to='events/images/', null=True, blank=True)
    video_url = models.URLField(blank=True)

    def __str__(self):
        return self.title
