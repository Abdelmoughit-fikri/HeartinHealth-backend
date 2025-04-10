from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"", views.CardiacDiseasesViewSet, basename="cardiac-diseases-articles")


urlpatterns = [
    path("", include(router.urls)),
    path('upload-image/', views.upload_image, name='upload_image'),
]
