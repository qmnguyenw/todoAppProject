from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
import django_filters.rest_framework
from .serializers import TaskSerializer
from .models import Task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('completed',) # category task by attribute `completed`
    ordering = ('date_created',) # sorting by date_create
    search_fields = ('task_name', 'task_desc',) # search for each column of db

# class DueTaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all().order_by('-date_created').filter(completed=False)
#     serializer_class = TaskSerializer

# class CompletedTaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all().order_by('-date_created').filter(completed=True)
#     serializer_class = TaskSerializer