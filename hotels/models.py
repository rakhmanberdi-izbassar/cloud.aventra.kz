from django.db import models
from core.models import City

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels')
    country = models.CharField(max_length=255)
    description = models.TextField()
    stars = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='hotels/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class RoomType(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='room_types')
    name = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    max_guests = models.PositiveIntegerField()
    available_rooms = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='room_types/', blank=True, null=True)
    has_breakfast = models.BooleanField(default=False)
    has_wifi = models.BooleanField(default=False)
    has_tv = models.BooleanField(default=False)
    has_air_conditioning = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.hotel.name} - {self.name}"
