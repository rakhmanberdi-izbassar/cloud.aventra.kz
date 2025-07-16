from rest_framework import serializers
from .models import Hotel, RoomType
from core.models import City

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
    room_types = RoomTypeSerializer(many=True, read_only=True)
    city = serializers.StringRelatedField()

    class Meta:
        model = Hotel
        fields = '__all__'
