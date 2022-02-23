from django.db import models

TASK_STATUS = (
    ("New", "New"),
    ("Started", "Started"),
    ("Ongoing", "Ongoing"),
    ("In QA", "In QA"),
    ("Completed", "Completed"),
)


# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    createdOn = models.DateTimeField('date created', auto_now_add=True)
    updatedOn = models.DateTimeField('date updated', auto_now=True)
    status = models.CharField(max_length=50, choices=TASK_STATUS, default="New")


class SubTask(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    createdOn = models.DateTimeField('date created', auto_now_add=True)
    updatedOn = models.DateTimeField('date updated', auto_now=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=TASK_STATUS, default="New")