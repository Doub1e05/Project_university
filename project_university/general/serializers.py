from .models import Status
from rest_framework.serializers import ModelSerializer

class StatusSerializer(ModelSerializer):
    
    class Meta:
        model = Status
        fields = "__all__"