"""livelocationtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from userinfo import urls as userRouter
from devicelocation import urls as LocationRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/', include((userRouter, "userinfo"), namespace="user_api")),
    # path('api/v1/location/', include(("devicelocation.urls", "devicelocation"), namespace='devicelocation-api')),
    path('api/v1/location/', include((LocationRouter, "devicelocation"), namespace='location-api')),
    path(r'channels-api/', include('channels_api.urls'))

]
