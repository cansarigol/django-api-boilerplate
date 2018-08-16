
from django.conf.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('api/v1/',include('mobile_api.urls'), name="v1"),
    path('superadminsystemforsupertramps/', admin.site.urls),
]
