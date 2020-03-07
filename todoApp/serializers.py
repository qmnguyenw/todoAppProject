from rest_framework import serializers
from .models import Task
from django.contrib.auth import get_user_model

class TaskSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, default='images/none/none.jpg')
    doc = serializers.FileField(max_length=None, use_url=True, default='docs/none/none.txt')
    class Meta:
        model = Task
        fields = ('id', 'task_name', 'task_desc', 'completed', 'date_created', 'image', 'doc')

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    # override Create method
    def create(self, validated_data):
        user = get_user_model().objects.create(
            username = validated_data['username']
        )
        # we assume there is custome auth model or build-in auth model
        # custom auth model can we set by AUTH_USER_MODEL in settings.py
        user.set_password(validated_data['password']) # we dont want to serialize password because it has been hashed
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')