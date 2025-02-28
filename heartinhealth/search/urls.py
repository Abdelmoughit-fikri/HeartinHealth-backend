from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register the SearchViewSet
router = DefaultRouter()
router.register(r'', views.searcHinhViewSet, basename='search')

urlpatterns = [
    path('', include(router.urls)),  # This ensures /api/search/ works
]