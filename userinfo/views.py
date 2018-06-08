from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from .serializer import *
# Create your views here.


@permission_classes((AllowAny,))
class RegistrationViewSet(ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer

    @csrf_exempt
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        Token.objects.create(user=serializer.instance)
        response = {"status": status.HTTP_201_CREATED, "message": "The user is submitted"}
        return Response(response, status=status.HTTP_201_CREATED)


@permission_classes((AllowAny,))
class LoginView(APIView):
    queryset = User.objects.all()

    def post(self, request, format=None):
        data = request.data
        username = data.get("username", None)
        password = data.get("password", None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                token = Token.objects.get(user=user)
                response = {"token" : token.key, "username":username}
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {"status": status.HTTP_404_NOT_FOUND, "message": "User is not active."}
                return Response(response,status=status.HTTP_404_NOT_FOUND)
        else:
            response = {"status": status.HTTP_404_NOT_FOUND, "message": "You have entered an invalid username or password"}
            return Response(response, status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    queryset = User.objects.all()
    authentication_classes = [TokenAuthentication,]

    def post(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_200_OK)


















