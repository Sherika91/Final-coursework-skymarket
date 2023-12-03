from requests import Response
from rest_framework import viewsets, pagination, status
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.models import Comment
from ads.permissions import IsOwnerOrAdmin
from ads.serializers import CommentSerializer, CommentCreateSerializer, CommentRetrieveSerializer


class CommentPaginator(pagination.PageNumberPagination):
    page_size = 10


class CommentViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'patch']
    pagination_class = CommentPaginator
    queryset = Comment.objects.all().order_by('-created_at')
    default_permission = [AllowAny, ]
    permissions = {
        'create': [IsAuthenticated],
        'list': [AllowAny],
        'retrieve': [AllowAny],
        'partial_update': [IsOwnerOrAdmin],
        'update': [IsOwnerOrAdmin],
        'destroy': [IsOwnerOrAdmin],
    }
    default_serializer = CommentSerializer
    serializer_classes = {
        'create': CommentCreateSerializer,
        'list': CommentSerializer,
        'retrieve': CommentRetrieveSerializer,
    }

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
