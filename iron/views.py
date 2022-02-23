from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import authentication_classes, permission_classes
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action

from .models import User
from .serializers import UserSerializer


@authentication_classes([])
@permission_classes([])
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'patch']

    @action(detail=True, methods=['POST'], url_path='password', url_name='password')
    def password(self, request, *args, **kwargs):
        """Does something on single item."""
        queryset = User.objects.exclude(serialized=None)
        # print("queryset", queryset)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
