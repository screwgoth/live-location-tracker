from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.response import Response

from .serializer import *


@permission_classes((AllowAny,))
class LocationViewSet(viewsets.ModelViewSet):
    queryset = DeviceLocation.objects.all()
    serializer_class = LocationSerializer
    second_serializer_class = ListLocationSerializer

    # def get_queryset(self):
    #     queryset = DeviceLocation().get_lat_long()
    #     return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'list':
            return self.second_serializer_class
        else:
            return self.serializer_class

