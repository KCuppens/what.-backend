"""
URL configuration for settings project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view


api_patterns = [
    path("users/", include("apps.users.api.v1.urls")),
    path("products/", include("apps.products.api.v1.urls")),
    path("carts/", include("apps.carts.api.v1.urls")),
]

urlpatterns = [
    path("api/v1/", include(api_patterns)),
    path(
        "openapi",
        get_schema_view(
            title="What. API",
            description="API endpoints for Users and Products",
            version="1.0.0",
            permission_classes=[],
            public=True,
        ),
        name="openapi-schema",
    ),
    path(
        "redoc/",
        TemplateView.as_view(
            template_name="redoc.html", extra_context={"schema_url": "openapi-schema"}
        ),
        name="redoc",
    ),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    try:
        urlpatterns += [
            path("__debug__/", include("debug_toolbar.urls")),
        ]
    except ImportError:
        pass
