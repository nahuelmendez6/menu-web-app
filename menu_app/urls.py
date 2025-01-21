"""
URL configuration for menu_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración de la documentación Swagger  http://localhost:8000/swagger/
schema_view = get_schema_view(
    openapi.Info(
        title="API de Menú Virtual",
        default_version='v1',
        description="Documentación de la API",
    ),
    public=True,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('manage/menu/', include('products.urls')),
    path('menu/', include('public_menu.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Ruta de Swagger
]
