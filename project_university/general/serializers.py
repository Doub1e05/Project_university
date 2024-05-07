from .models import Status, Thread, Works, Subjects, User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

class UserLoginSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField()

    def check_user(self, clean_data):
        user = authenticate(login=clean_data['login'], password=clean_data['password'])

        if not user:
            raise ValidationError('User Not Found')
        
        return user

class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ("id", "login", "last_name", "first_name", "surname", "role", "telegram", "thread")

class ThreadSerializer(ModelSerializer):

    class Meta:
        model = Thread
        fields = "__all__"

class WorksSerializer(ModelSerializer):

    class Meta:
        model = Works
        fields = "__all__"

class SubjectsSerializer(ModelSerializer):

    class Meta:
        model = Subjects
        fields = "__all__"

class StatusSerializer(ModelSerializer):
    work = WorksSerializer()
    student = UserSerializer()

    class Meta:
        model = Status
        fields = "__all__"
