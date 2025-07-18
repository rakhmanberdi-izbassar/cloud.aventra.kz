from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Tour
from .serializers import TourSerializer
from .models import Location
from .serializers import LocationSerializer
from rest_framework import generics
from .models import City
from .serializers import CitySerializer

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all().select_related('user', 'location').prefetch_related('images')
    serializer_class = TourSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request
        search = request.query_params.get('search')
        date = request.query_params.get('date')
        people = request.query_params.get('people')
        date_to = request.query_params.get('date_to')
        price_max = request.query_params.get('price_max')
        volume_max = request.query_params.get('volume_max')
        user_id = request.query_params.get('user_id')
        location_id = request.query_params.get('location_id')

        if search:
            queryset = queryset.filter(Q(name__icontains=search) | Q(description__icontains=search))
        if date:
            queryset = queryset.filter(date__lte=date)
        if people:
            queryset = queryset.filter(volume__gte=people)
        if date_to:
            queryset = queryset.filter(date__lte=date_to)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)
        if volume_max:
            queryset = queryset.filter(volume__lte=volume_max)
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        if location_id:
            queryset = queryset.filter(location_id=location_id)

        return queryset

    @action(detail=True, methods=['post'])
    def purchase(self, request, pk=None):
        tour = self.get_object()
        seats = int(request.data.get('seats', 1))

        try:
            tour.decrease_volume(seats)
            return Response({'message': 'Тур сәтті сатып алынды', 'remaining_volume': tour.volume})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def featured(self, request):
        tours = Tour.objects.filter(featured=True).prefetch_related('images').order_by('-id')[:10]
        serializer = self.get_serializer(tours, many=True)
        return Response({'success': True, 'data': serializer.data})

class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.select_related('city').all()
    serializer_class = LocationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
