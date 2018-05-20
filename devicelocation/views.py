import datetime
import time

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from devicelocation.models import DeviceLocation


# Create your views here.
class DeviceLocationListAPIView(generics.ListAPIView):
    queryset = DeviceLocation.objects.all()
    print("Got DeviceLocation GET Request")


class DeviceLocationCreateAPIView(generics.CreateAPIView):
    queryset = DeviceLocation.objects.all()
    print("Got DeviceLocation POST Request")
