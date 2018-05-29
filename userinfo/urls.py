from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from .views import *


router = routers.SimpleRouter()
router.register(r'register', RegistrationViewSet)
# router.register(r'login', LoginView.as_view(), base_name="login")
# router.register(r'logout', LogoutView.as_view(), base_name="logout")


urlpatterns = [
    url(r'login/$', LoginView.as_view(), name='login'),
    url(r'logout/$', LogoutView.as_view(), name='logout'),
    url(r'^users/', include((router.urls, 'app_name'))),

]






