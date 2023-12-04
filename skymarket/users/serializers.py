from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()
# TODO Здесь нам придется переопределить сериалайзер, который использует djoser
# TODO для создания пользователя из за того, что у нас имеются нестандартные поля


class UserRegistrationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "email", "first_name", "last_name", "password", "phone", 'image')


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "phone", 'image')
