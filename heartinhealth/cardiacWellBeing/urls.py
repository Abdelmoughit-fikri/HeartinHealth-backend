from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(
    r"", views.CardiacWellBeingViewSet, basename="cardiac-well-being-articles"
)


urlpatterns = [
    path("", include(router.urls)),
]
