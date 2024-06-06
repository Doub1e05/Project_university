from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from django.middleware.csrf import get_token
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from .validations import validate_login, validate_password
from django.contrib.auth import login, logout

from .models import Status, Thread, Works, Subjects

from .serializers import StatusSerializer, UserLoginSerializer, UserSerializer,\
        ThreadSerializer, WorksSerializer, SubjectsSerializer
from django.middleware.csrf import CsrfViewMiddleware
import cv2
import easyocr
from PIL import Image
import numpy as np
import io

class ProcessImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES['image']
        img = Image.open(file_obj)
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        reader = easyocr.Reader(["ru"])
        result = reader.readtext(img, detail=1, paragraph=False)

        digit_result = []
        for i in result:
            if i[1].isdigit():
                digit_result.append(i[1])

        return Response({'digits': digit_result}, status=status.HTTP_200_OK)    


class UserLogin(APIView):
    """
    Авторизация пользователя
    """
    # permission_classes = ()
    # authentication_classes = ()
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
    # permission_classes = ()
    # authentication_classes = ()
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        logout(request)
        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie('sessionid')
        return response
    
class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    # permission_classes = ()
    # authentication_classes = ()
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'profile': serializer.data}, status=status.HTTP_200_OK)

class ThreadView(ListCreateAPIView):
    """
    Полный список потоков
    """
    permission_classes = ()
    authentication_classes = ()

    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (SessionAuthentication,)

    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

class ThreadAPIViewAction(APIView):
    """
    Определённый поток
    """  
    permission_classes = ()
    authentication_classes = ()
    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (SessionAuthentication,)

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
    permission_classes = ()
    authentication_classes = ()
    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (SessionAuthentication,)
    
    queryset = Works.objects.all()
    serializer_class = WorksSerializer

class WorksAPIViewAction(APIView):
    """
    Определённая лабораторная работа
    """ 

    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (SessionAuthentication,)
    permission_classes = ()
    authentication_classes = ()

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
    permission_classes = ()
    authentication_classes = ()
    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (SessionAuthentication,)
    
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer

class SubjectsAPIViewAction(APIView):
    """
    Определённый предмет
    """  

    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (SessionAuthentication,)
    permission_classes = ()
    authentication_classes = ()
    
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

    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class StatusAPIViewAction(APIView):
    """
    Список работы определённого студента
    """ 

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
