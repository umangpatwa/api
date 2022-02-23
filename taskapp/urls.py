from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import TaskViewSet, SubTaskViewSet, SubTaskGetViewSet

router = SimpleRouter()

router.register('task', TaskViewSet)

router.register('sub-task', SubTaskViewSet)

router.register('subtasks', SubTaskGetViewSet)


urlpatterns = [
    url('<int:task>/subtasks/', SubTaskGetViewSet.as_view({"get": "subtasks"}), name='subtasks'),
] + router.urls
