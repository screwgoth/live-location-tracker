import datetime
import time
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from devicelocation.models import DeviceLocation
from .serializer import *
from rest_framework import viewsets
from django.views.generic import TemplateView

@permission_classes((AllowAny,))
class LocationViewSet(viewsets.ModelViewSet):
    queryset = DeviceLocation.objects.all()
    serializer_class = LocationSerializer
    second_serializer_class = ListLocationSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return self.second_serializer_class
        else:
            return self.serializer_class

    def get_queryset(self):
        print("In Get")
        user = self.request.user
        print(user,  "user")
        queryset = DeviceLocation.objects.filter(user=user)
        return queryset

    def create(self, request, *args, **kwargs):
        print("**************", request.data, "**************")
        return super(LocationViewSet, self).create(request, *args, **kwargs)
