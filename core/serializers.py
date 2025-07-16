from rest_framework import serializers
from .models import Tour, TourImage
from .models import Location, City

class TourImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourImage
        fields = ['id', 'image_path']

class TourSerializer(serializers.ModelSerializer):
    images = TourImageSerializer(many=True, read_only=True)

    class Meta:
        model = Tour
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(), source='city', write_only=True
    )

    class Meta:
        model = Location
        fields = ['id', 'name', 'city', 'city_id']