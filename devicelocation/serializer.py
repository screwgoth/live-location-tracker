from rest_framework import serializers
from devicelocation.models import DeviceLocation


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLocation
        fields = "__all__"


class ListLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLocation
        fields = ["lat", "long"]



