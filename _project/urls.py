
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('api/v1/app/', include('app.urls')),
    path('admin/', admin.site.urls),
]
