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


# Create your views here.
class DeviceLocationListAPIView(generics.ListAPIView):
    queryset = DeviceLocation.objects.all()
    serializer_class = DeviceLocationListSerializer


class DeviceLocationCreateAPIView(generics.CreateAPIView):
    queryset = DeviceLocation.objects.all()
    serializer_class = DeviceLocationSerializer

    def creat(self, request, *args, **kwargs):
        serializer = DeviceLocationSerializer(data=request,
                                                context={'request': request})

        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


@permission_classes((AllowAny,))
class LocationViewSet(viewsets.ModelViewSet):
    queryset = DeviceLocation.objects.all()
    serializer_class = LocationSerializer

    def create(self, request, *args, **kwargs):
        print("**************", request.data, "**************")
        return super(LocationViewSet, self).create(request, *args, **kwargs)



