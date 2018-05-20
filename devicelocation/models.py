from django.db import models


# Create your models here.
class DeviceLocation(models.Model):
    deviceID = models.CharField(max_length=50)
    lat = models.CharField(max_length=50)
    long = models.CharField(max_length=50)
    timestamp = models.CharField(max_length=50)
    speed = models.CharField(max_length=50)
    accuracy = models.CharField(max_length=50)

    class Meta:
        verbose_name = "DeviceLocation"

    def __unicode__(self):
        return self.name
