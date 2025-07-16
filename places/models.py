from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()
    images = models.JSONField(blank=True, null=True)
    things_to_do = models.JSONField(blank=True, null=True)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name

    @property
    def coordinates(self):
        return {"lat": self.lat, "lng": self.lng}

    @coordinates.setter
    def coordinates(self, value):
        self.lat = value.get("lat")
        self.lng = value.get("lng")