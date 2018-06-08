from django.conf.urls import url
from django.urls import include
from devicelocation import views as device_views
from rest_framework import routers
from devicelocation.views import LocationViewSet

router = routers.SimpleRouter()
router.register(r'log', LocationViewSet)

urlpatterns = [
    url(r'', include((router.urls, 'devicelocation'))),
]
