from django.shortcuts import render
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .models import Task, SubTask
from .serializers import TaskSerializer, SubTaskSerializer
from rest_framework.response import Response


# Create your views here.
@authentication_classes([])
@permission_classes([])
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'patch']


@authentication_classes([])
@permission_classes([])
class SubTaskViewSet(ModelViewSet):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'patch']



@authentication_classes([])
@permission_classes([])
class SubTaskGetViewSet(ModelViewSet):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    http_method_names = ['get']

    lookup_field = 'task'

    @action(detail=True, methods=['GET'], url_path='subtasks', url_name='subtasks')
    def subtasks(self, request, *args, **kwargs):
        """Does something on single item."""
        queryset = SubTask.objects.filter(task=kwargs['task'])
        serializer = SubTaskSerializer(queryset, many=True)
        return Response(serializer.data)
