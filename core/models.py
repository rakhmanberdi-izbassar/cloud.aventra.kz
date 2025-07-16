from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255)
    img = models.URLField()  # немесе models.ImageField() — егер файл түрінде сақталса
    description = models.TextField()
    city_code = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='locations' , null=True)

    def __str__(self):
        return f"{self.name} ({self.city.name})"

class Tour(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.PositiveIntegerField()
    date = models.DateField()
    image = models.ImageField(upload_to='tours/', null=True, blank=True)
    featured = models.BooleanField(default=False)

    def decrease_volume(self, seats):
        if self.volume < seats:
            raise ValueError("Көрсетілген орын саны жеткіліксіз.")
        self.volume -= seats
        self.save()

    def increase_volume(self, seats):
        self.volume += seats
        self.save()

class TourImage(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='images')
    image_path = models.ImageField(upload_to='tours/')
