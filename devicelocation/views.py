from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .serializer import *


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
