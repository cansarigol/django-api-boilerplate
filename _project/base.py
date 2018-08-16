import json
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import serializers

import collections

class BaseApiResponse(serializers.Serializer):
    is_success = serializers.BooleanField()
    error_message = serializers.CharField(max_length=200)
    error_code = serializers.CharField(max_length=100)


class BaseApiView(APIView):
    """
    My base class view for whole apiview classes
    """
    query_set = None
    def get_serializer(self, *args, **kwargs):
        if not self.api_request:
            return None
        serializer_class = self.api_request
        kwargs['context'] = {
            'request': self.api_request,
            'view': self,
        }
        return serializer_class(*args, **kwargs)
    def __init__(self, api_response, data_response, api_request):
        self.init_data = {
            "is_success": True, 
            "error_message": "", 
            "error_code": "",
            "data": None
        }
        self.api_response = api_response
        self.data_response = data_response
        self.api_request = api_request

    def prepare_response(self, with_error="", error_code=""):
        if with_error:
            self.init_data["is_success"] = False
            self.init_data["error_message"] = with_error
            self.init_data["error_code"] = error_code

        serializer = self.api_response(self.init_data)
        return Response(serializer.data)
    def get_serializer_request(self, request):
        return self.api_request(data=request.data)
    def get_request_data(self, request):
        return request.data
    def get_data(self, request):
        serializer_request = self.api_request(data=request.data)
        if not serializer_request.is_valid():
            return None, serializer_request.errors
        return serializer_request.data, None
    def post(self, request):
        try:
            if not self.init_data["data"]:
                query_data = self.query_set
                if not query_data:
                    return self.prepare_response("Result not found", "result_not_found")
                self.init_data["data"] = self.data_response(self.query_set, many=isinstance(query_data, collections.Iterable)).data
        except Exception as ex:
            return self.prepare_response(ex, "exception")

        return self.prepare_response()
