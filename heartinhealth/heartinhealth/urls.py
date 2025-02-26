from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularRedocView, SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('heartinhealthAdmin/', admin.site.urls),
    path('cardiac-diseases/', include('cardiacDiseases.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

admin.site.site_header = 'Heart in Health'