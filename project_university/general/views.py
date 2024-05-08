from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication

from .validations import validate_login, validate_password
from django.contrib.auth import login, logout

from .models import Status, Thread, Works, Subjects

from .serializers import StatusSerializer, UserLoginSerializer, UserSerializer,\
        ThreadSerializer, WorksSerializer, SubjectsSerializer

# from rest_framework.permissions import BasePermission
#
# Права для пользователей (планируется)
# class IsTeacher(BasePermission):
#     """
#     Разрешение для преподавателей
#     """
#     def has_permission(self, request, view):
#         # Проверяем, является ли текущий пользователь преподавателем
#         return request.user.role == 'Teacher'

# class IsStudent(BasePermission):
#     """
#     Разрешение для студентов
#     """
#     def has_permission(self, request, view):
#         # Проверяем, является ли текущий пользователь студентом
#         return request.user.role == 'Student'

class UserLogin(APIView):
    """
    Авторизация пользователя
    """
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data

        assert validate_login(data)
        assert validate_password(data)

        serializer = UserLoginSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)

class UserLogout(APIView):
    """
    Выход пользователя
    """
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
    
class UserView(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	
	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response({'profile': serializer.data}, status=status.HTTP_200_OK)

class ThreadView(ListCreateAPIView):
    """
    Полный список потоков
    """

    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

class ThreadAPIViewAction(APIView):
    """
    Определённый поток
    """  

    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request, id):
        try:
            data = Thread.objects.get(id=id)
        
        except Thread.DoesNotExist:
            message = {"message": "Thread not found"}
            return Response(message, status=status.HTTP_404_NOT_FOUND)

        serializer = ThreadSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WorksView(ListCreateAPIView):
    """
    Полный список лабораторных работ
    """

    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    
    queryset = Works.objects.all()
    serializer_class = WorksSerializer

class WorksAPIViewAction(APIView):
    """
    Определённая лабораторная работа
    """ 

    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request, id):
        try:
            data = Works.objects.get(id=id)
        
        except Works.DoesNotExist:
            message = {"message": "Work not found"}
            return Response(message, status=status.HTTP_404_NOT_FOUND)

        serializer = WorksSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        try:
            data = Works.objects.get(id=id)

        except Works.DoesNotExist:
            message = {"message: Work not found"}
            return  Response(message, status=status.HTTP_404_NOT_FOUND)

        data.delete()
        return Response({"message": "Work deleted"}, status=status.HTTP_204_NO_CONTENT)


class SubjectsView(ListCreateAPIView):
    """
    Полный список предметов
    """

    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer

class SubjectsAPIViewAction(APIView):
    """
    Определённый предмет
    """  

    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    
    def get(self, request, id):
        try:
            data = Subjects.objects.get(id=id)
        
        except Subjects.DoesNotExist:
            message = {"message": "Subject not found"}
            return Response(message, status=status.HTTP_404_NOT_FOUND)

        serializer = SubjectsSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StatusAPIView(ListCreateAPIView):
    """
    Полный список статусов лабораторных работ у каждого студента
    """
    permission_classes = ()
    authentication_classes = ()

    permission_classes = ()
    authentication_classes = ()

    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class StatusAPIViewAction(APIView):
    """
    Список работы определённого студента
    """ 

    permission_classes = ()
    authentication_classes = ()

    permission_classes = ()
    authentication_classes = ()

    def get(self, request, id):
        try:
            data = Status.objects.get(id=id)
        
        except Status.DoesNotExist:
            message = {"message": "Status not found"}
            return Response(message, status=status.HTTP_404_NOT_FOUND)

        serializer = StatusSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        try:
            data = Status.objects.get(id=id)

        except:
            message = {"message": "Status not found"}
            return Response(message, status=status.HTTP_404_NOT_FOUND)

        serializer = StatusSerializer(data, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            data = Status.objects.get(id=id)
        
        except Status.DoesNotExist:
            message = {"message": "Status not found"}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        data.delete()
        return Response({"message": "Status deleted"}, status=status.HTTP_204_NO_CONTENT)
