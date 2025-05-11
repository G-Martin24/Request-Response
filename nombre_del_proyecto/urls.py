
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('request/', include('request.urls')),  # Incluye las URLs de tu aplicación 'request' bajo la ruta '/request/'
]