from channels_api.bindings import ResourceBinding
from .models import DeviceLocation
from .serializer import ListLocationSerializer, LocationSerializer


class LocationBinding(ResourceBinding):
    model = DeviceLocation
    stream = "locations"
    serializer_class = ListLocationSerializer
    queryset = DeviceLocation.objects.all()

