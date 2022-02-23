from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token, ObtainAuthToken
from iron.views import UserViewSet
from django.urls import path

router = routers.SimpleRouter()


urlpatterns = [
    url(r'^', include(router.urls)),
    url('auth/', include('dj_rest_auth.urls')),
    url('auth/register/', include('dj_rest_auth.registration.urls')),
    path('auth/token/', obtain_auth_token),
]
