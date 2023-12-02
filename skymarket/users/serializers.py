from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
# TODO Здесь нам придется переопределить сериалайзер, который использует djoser
# TODO для создания пользователя из за того, что у нас имеются нестандартные поля


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        user.set_password(validated_data.get('password'))
        user.save()

        return user


class CurrentUserSerializer(serializers.ModelSerializer):
    pass
