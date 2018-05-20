from django.conf.urls import url
from devicelocation import views as device_views


urlpatterns = [
    url(r'^$', device_views.DeviceLocationListAPIView.as_view(), name='location-list'),
    url(r'^location/$', device_views.DeviceLocationCreateAPIView.as_view(), name='location-create')
]
