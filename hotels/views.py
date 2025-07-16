from rest_framework import viewsets
from .models import Hotel, RoomType
from .serializers import HotelSerializer, RoomTypeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.prefetch_related('room_types').all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]