from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from apps.views import ProductCreateAPIView
from root.settings import STATIC_URL, STATIC_ROOT

urlpatterns = [
    path('', include('apps.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.urls')),
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]+static(STATIC_URL, document_root=STATIC_ROOT)
