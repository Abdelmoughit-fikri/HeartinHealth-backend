from django.shortcuts import render
from drf_spectacular.views import SpectacularSwaggerView
from django.conf import settings
from django.http import HttpResponseForbidden

def info_page(request):
    secretKey = settings.SECRET_DOCS_TOKEN
    return render(request, 'info.html', {'secret_token': secretKey})

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def custom_500_view(request):
    return render(request, '500.html', status=500)

class TokenProtectedSpectacularSwaggerView(SpectacularSwaggerView):
    def dispatch(self, request, *args, **kwargs):
        # Expect a token in the URL query parameters (e.g., ?secret=...)
        token = request.GET.get("secret", "")
        if token != settings.SECRET_DOCS_TOKEN:
            return HttpResponseForbidden("Forbidden: visitors are not allowed to see the docs")
        return super().dispatch(request, *args, **kwargs)
