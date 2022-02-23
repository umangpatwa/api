from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from drf_yasg.generators import OpenAPISchemaGenerator
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


class HttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema


# from accounts.urls import urlpatterns as api_v1
schema_view = get_schema_view(
    openapi.Info(
        title="Task Management APIs",
        default_version='v2.5.0',
        description="The purpose of this online document is to describe the APIs",
        terms_of_service="https://www.microgridlabs.com",
        contact=openapi.Contact(email="patwa.jain@yahoo,com"),
        license=openapi.License(name="Proprietary/Closed License"),
    ),

    public=True,
    generator_class=HttpAndHttpsSchemaGenerator,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('iron.urls')),
    url('', include('taskapp.urls')),
    # url(r'^(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
