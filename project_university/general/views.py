from .models import Status, User
from .serializers import StatusSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework import status

class StatusAPIView(ListCreateAPIView):

    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class StatusAPIViewAction(APIView):
     
    def get(self, request, id):
        try:
            data = Status.objects.get(id=id)
        
        except Status.DoesNotExist:
            message = {"message": "Object not found"}
            return Response(message, status=status.HTTP_404_NOT_FOUND)

        serializer = StatusSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        try:
            data = Status.objects.get(id=id)

        except:
            message = {"message": "Object not found"}
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
            message = {"message": "Object not found"}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        data.delete()
        return Response({"message": "Object deleted"}, status=status.HTTP_204_NO_CONTENT)