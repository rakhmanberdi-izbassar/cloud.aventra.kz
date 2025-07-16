from rest_framework import serializers
from .models import Event, EventType
from core.models import City  # City моделі core стартапында орналасқан

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']

class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ['id', 'name']

class EventSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(), source='city', write_only=True
    )
    event_type = EventTypeSerializer(read_only=True)
    event_type_id = serializers.PrimaryKeyRelatedField(
        queryset=EventType.objects.all(), source='event_type', write_only=True
    )

    class Meta:
        model = Event
        fields = [
            'id', 'user', 'city', 'city_id', 'event_type', 'event_type_id',
            'title', 'description', 'start_date', 'end_date',
            'location_name', 'address', 'latitude', 'longitude',
            'price_info', 'organizer', 'phone', 'email', 'website',
            'image', 'video_url'
        ]