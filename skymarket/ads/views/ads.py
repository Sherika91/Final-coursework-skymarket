from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, pagination, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action

from ads.serializers import (
    AdSerializer,
    AdDetailSerializer,
    AdListSerializer,
    AdCreateSerializer)

from ads.filters import AdFilter
from ads.models import Ad
from ads.permissions import IsOwnerOrAdmin


class AdPaginator(pagination.PageNumberPagination):
    page_size = 10


class AdViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'patch']
    pagination_class = AdPaginator
    queryset = Ad.objects.all()
    default_permission = [AllowAny, ]
    permissions = {
        'create': [IsAuthenticated],
        'list': [AllowAny],
        'retrieve': [AllowAny],
        'partial_update': [IsOwnerOrAdmin],
        'update': [IsOwnerOrAdmin],
        'destroy': [IsOwnerOrAdmin],
    }

    default_serializer = AdSerializer
    serializer_classes = {
        'create': AdCreateSerializer,
        'list': AdListSerializer,
        'retrieve': AdDetailSerializer,
    }

    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # @extend_schema(summary='My Ads', responses=AdListSerializer)
    # @action(detail=False, methods=['get'], permission_classes=[IsOwnerOrAdmin], url_path='me')
    # def my_ads(self, request):
    #     ads = Ad.objects.filter(author_id=self.request.user.id)
    #     paginator = AdPaginator()
    #     page = paginator.paginate_queryset(ads, request)
    #
    #     return paginator.get_paginated_response(AdListSerializer(page, many=True).data)


class UserAdsAPIView(generics.ListAPIView):
    serializer_class = AdListSerializer
    permission_classes = [IsOwnerOrAdmin,]
    pagination_class = AdPaginator

    def get_queryset(self):
        user = self.request.user
        return Ad.objects.filter(author_id=user.id)

