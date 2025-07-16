from rest_framework import viewsets, filters
from .models import Event, EventType
from .serializers import EventSerializer, EventTypeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.select_related('city', 'event_type', 'user').all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['city', 'event_type', 'start_date']
    search_fields = ['title', 'description', 'location_name']

class EventTypeViewSet(viewsets.ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]