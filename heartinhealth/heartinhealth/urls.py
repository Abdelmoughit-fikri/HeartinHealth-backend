from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularRedocView,
    SpectacularAPIView,
    SpectacularSwaggerView,
)


urlpatterns = [
    path("heartinhealthAdmin/", admin.site.urls),
    path("api/cardiacDiseases/", include("cardiacDiseases.urls")),
    path("api/symptoms&diagnosis/", include("cardiacSymptomsAndDiagnosis.urls")),
    path("api/cardiacWellBeing/", include("cardiacWellBeing.urls")),
    path("api/cardiacInnovations/", include("cardiacInnovations.urls")),
    path("api/search/", include("search.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Heart in Health"
admin.site.site_title = "HeartinHealth"
