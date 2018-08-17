# -*- coding: utf-8 -*-
from .serializers import AppApiResponse, AppDataResponse, AppRequest
from .models import Apps
from _project.base import BaseApiView

class GetAppView(BaseApiView):
    """
    Get apps
    """
    def __init__(self, *args, **kwargs):
        super(GetAppView, self).__init__(AppApiResponse, AppDataResponse, AppRequest)

    def post(self, request):
        data, error = self.get_data(request)
        if error:
            return self.prepare_response(error, "model_not_valid")

        self.query_set = Apps.objects.get_from_name(data["name"])

        return super(GetAppView, self).post(request)
