from django.conf.urls import url
from django.urls import include
from devicelocation import views as device_views
from rest_framework import routers
from devicelocation.views import LocationViewSet

router = routers.SimpleRouter()
router.register(r'log', LocationViewSet)

urlpatterns = [
    # url(r'^$', device_views.DeviceLocationListAPIView.as_view(), name='location-list'),
    # url(r'^location/$', device_views.DeviceLocationCreateAPIView.as_view(), name='location-create'),
    # url(r'^log/$', device_views.LocationViewSet, name='location-create')
    url(r'', include((router.urls, 'devicelocation'))),
]
