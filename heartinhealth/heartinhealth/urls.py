from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

# from rest_framework_api_key.permissions import HasAPIKey


# schema_view = get_schema_view(
#     openapi.Info(
#         title="My API",
#         default_version='v1',
#         description="API Documentation",
#     ),
#     public=False,  # Set to False to restrict public access
#     permission_classes=[HasAPIKey],  # Require authentication
# )
secretKey = settings.SECRET_DOCS_TOKEN
urlpatterns = [
    path("", include("info.urls")),
    path("heartinhealthAdmin/", admin.site.urls),
    path("api/cardiacDiseases/", include("cardiacDiseases.urls")),
    path("api/symptoms/", include("cardiacSymptomsAndDiagnosis.urls")),
    path("api/cardiacWellBeing/", include("cardiacWellBeing.urls")),
    path("api/cardiacInnovations/", include("cardiacInnovations.urls")),
    path("api/search/", include("search.urls")),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Heart in Health"
admin.site.site_title = "HeartinHealth"
