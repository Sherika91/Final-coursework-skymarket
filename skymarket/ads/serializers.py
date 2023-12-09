from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.phonenumber import to_python
from requests import Response
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError

from ads.models import Ad, Comment
from users.serializers import PhoneNumberFieldSerializer


# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    ad = serializers.ReadOnlyField(source='ad.title')
    ad_id = serializers.ReadOnlyField(source='ad.pk')

    class Meta:
        model = Comment
        fields = '__all__'


# Comment Create Serializer
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'ad', 'text', 'description',


class CommentRetrieveSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    ad = serializers.ReadOnlyField(source='ad.title')
    ad_id = serializers.ReadOnlyField(source='ad.pk')

    class Meta:
        model = Comment
        fields = '__all__'


# Ads Serializers for Crud actions
class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = 'title', 'price', 'description',


class AdDetailSerializer(serializers.ModelSerializer):
    phone = PhoneNumberFieldSerializer(source='author.phone', read_only=True)
    author = serializers.ReadOnlyField(source='author.email')
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    author_id = serializers.ReadOnlyField(source='author.pk')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Ad
        fields = ['pk', 'title', 'price', 'description', 'phone', 'author', 'author_first_name', 'author_last_name',
                  'author_id', 'comments']


class AdListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='email', read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'
