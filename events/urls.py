from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import EventViewSet, EventTypeViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'event-types', EventTypeViewSet, basename='eventtype')

urlpatterns = [
    path('', include(router.urls)),
]