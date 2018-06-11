from django.contrib.auth.models import User
from django.db import models


class DeviceLocation(models.Model):
    lat = models.CharField(max_length=50)
    long = models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name="location_user", on_delete="PROTECT",null=True)
    annotation = models.CharField(max_length=50, null=True, blank=True)
    satellites = models.CharField(max_length=50, null=True, blank=True)
    altitude = models.CharField(max_length=50, null=True, blank=True)
    android_id = models.CharField(max_length=100, null=True, blank=True)
    speed = models.CharField(max_length=50, null=True, blank=True)
    accuracy = models.CharField(max_length=50, null=True, blank=True)
    direction = models.CharField(max_length=50, null=True, blank=True)
    provider = models.CharField(max_length=50, null=True, blank=True)
    timestamp = models.CharField(max_length=50, null=True, blank=True)
    utc_time = models.CharField(max_length=50, null=True, blank=True)
    start_timestamp = models.CharField(max_length=50, null=True, blank=True)
    battery = models.CharField(max_length=50, null=True, blank=True)
    serial = models.CharField(max_length=50, null=True, blank=True)
    activity = models.CharField(max_length=50, null=True, blank=True)
    file = models.CharField(max_length=50, null=True, blank=True)
    profile = models.CharField(max_length=50, null=True, blank=True)
    hdop = models.CharField(max_length=50, null=True, blank=True)
    vdop = models.CharField(max_length=50, null=True, blank=True)
    pdop = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "DeviceLocation"

    def __unicode__(self):
        return self.name
