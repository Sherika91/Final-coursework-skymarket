from requests import Response
from rest_framework import serializers, status

from ads.models import Ad, Comment


# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    ad = serializers.ReadOnlyField(source='ad.title')

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
    phone = serializers.ReadOnlyField(source='author.phone')
    author = serializers.ReadOnlyField(source='author.email')
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    author_id = serializers.ReadOnlyField(source='author.pk')

    class Meta:
        model = Ad
        fields = ['pk', 'title', 'price', 'description', 'phone', 'author', 'author_first_name', 'author_last_name',
                  'author_id']


class AdListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='email', read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'
