from rest_framework import serializers
from .models import Task, SubTask


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'taskTitle', 'taskDescription', 'createdOn', 'updatedOn', 'status']


class SubTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubTask
        fields = ['id', 'taskTitle', 'taskDescription', 'createdOn', 'updatedOn', 'status', 'task']