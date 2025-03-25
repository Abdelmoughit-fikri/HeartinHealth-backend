from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView
from .views import TokenProtectedSpectacularSwaggerView
from django.conf.urls import handler404,handler500
from .views import custom_404_view, custom_500_view

handler404 = custom_404_view
handler500 = custom_500_view
urlpatterns = [
    path('', views.info_page, name='info_page'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', TokenProtectedSpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
