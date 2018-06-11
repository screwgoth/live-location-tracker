from django.contrib import admin
from .models import DeviceLocation


# Register your models here.
class DeviceLocationModelAdmin(admin.ModelAdmin):
    list_display = ['android_id', 'lat', 'long', 'speed','serial', 'accuracy', 'timestamp', 'server_timestamp']

    class Meta:
        model = DeviceLocation


admin.site.register(DeviceLocation, DeviceLocationModelAdmin)
