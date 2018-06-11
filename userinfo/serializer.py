from rest_framework import serializers, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all(),
                                                                 message="A user with that username already exist.")])
    email = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all(),
                                                              message="A user with that email already exist.")])

    class Meta:
        model = User
        fields = ("username", "email", "password",)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance