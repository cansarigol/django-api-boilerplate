from rest_framework import serializers
from .models import Apps
from _project.base import BaseApiResponse

class AppDataResponse(serializers.ModelSerializer):
    class Meta:
        model = Apps
        fields = ('id', 'code', 'name')

class AppApiResponse(BaseApiResponse):
    data = AppDataResponse(many=True)

class AppRequest(serializers.Serializer):
    name = serializers.CharField()