from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
import django_filters.rest_framework
from .serializers import TaskSerializer, UserSerializer
from .models import Task
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class TaskViewSet(viewsets.ModelViewSet):
    # authentication_classes = (TokenAuthentication, SessionAuthentication)
    authentication_classes = (BasicAuthentication, SessionAuthentication)
    # only Authenticated User can perform CRUD operation
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()  # use filter and ordering so remove order_by
    serializer_class = TaskSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('completed',)  # category task by attribute `completed`
    ordering = ('date_created',)  # sorting by date_create
    # search for each column of db, in here we can add '^', '=', '@', '$'
    search_fields = ('task_name', 'task_desc',)

# class DueTaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all().order_by('-date_created').filter(completed=False)
#     serializer_class = TaskSerializer

# class CompletedTaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all().order_by('-date_created').filter(completed=True)
#     serializer_class = TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)  # allow anyone can see

# class CreateUserView(CreateAPIView):
#     # createApiView provide only POST method
#     model = get_user_model()
#     # set permission as allowany to register
#     permission_classes = (AllowAny,)
#     serializer_class = UserSerializer
