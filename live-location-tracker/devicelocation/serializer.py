import time
from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User
from devicelocation.models import DeviceLocation


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLocation
        exclude = ("server_timestamp",)

    def create(self, validated_data):
        profile = validated_data.pop("profile")
        try:
            server_time = int(time.time())
            user = User.objects.get(username=profile)
            location = DeviceLocation.objects.create(user=user, server_timestamp=server_time, **validated_data)
            return location
        except User.DoesNotExist:
            raise ValidationError("Bad Request")


class ListLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceLocation
        fields = ["id", "lat", "long", ]










