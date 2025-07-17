from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet  # өз view классыңызды импорттаңыз

router = DefaultRouter()
router.register(r'hotels', HotelViewSet, basename='hotel')  # жол атауын нақты көрсетіңіз

urlpatterns = [
    path('', include(router.urls)),
]
