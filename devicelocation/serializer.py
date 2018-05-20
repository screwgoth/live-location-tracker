from rest_framework import serializers
from devicelocation.models import DeviceLocation


class DeviceLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLocation
        fields = ['deviceID','lat', 'long', 'speed', 'accuracy', 'timestamp']


class DeviceLocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLocation
        fields = ['deviceID', 'lat', 'long', 'speed', 'accuracy', 'timestamp']
