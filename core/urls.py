from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TourViewSet
from .views import CityViewSet

router = DefaultRouter()
router.register(r'tours', TourViewSet)
router.register(r'cities', CityViewSet, basename='city')

urlpatterns = [
    path('', include(router.urls)),
]
