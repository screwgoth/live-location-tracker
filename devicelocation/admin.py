from django.contrib import admin
from .models import DeviceLocation


# Register your models here.
class DeviceLocationModelAdmin(admin.ModelAdmin):
    list_display = ['deviceID', 'lat', 'long', 'speed', 'accuracy', 'timestamp']

    class Meta:
        model = DeviceLocation


admin.site.register(DeviceLocation, DeviceLocationModelAdmin)
