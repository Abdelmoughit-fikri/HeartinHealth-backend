from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubscriberViewSet,SendNewsletterViewSet

router = DefaultRouter()
router.register(r'', SubscriberViewSet, basename='newsletter-subscribers')
router.register(r'send-newsletter', SendNewsletterViewSet, basename='send-newsletter')


urlpatterns = [
    path('', include(router.urls)),
]
