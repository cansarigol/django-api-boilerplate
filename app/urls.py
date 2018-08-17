from django.urls import path
from .views import GetAppView

urlpatterns = [
    path('get-apps/', GetAppView),
]