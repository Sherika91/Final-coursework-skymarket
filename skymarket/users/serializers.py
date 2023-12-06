from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class PhoneNumberFieldSerializer(serializers.CharField):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return str(data)


class UserRegistrationSerializer(UserCreateSerializer):
    phone = PhoneNumberFieldSerializer()

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "email", "first_name", "last_name", "password", "phone", 'image')


class CurrentUserSerializer(serializers.ModelSerializer):
    phone = PhoneNumberFieldSerializer()

    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "phone", 'image')
