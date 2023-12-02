from django.urls import path, include

from ads.apps import SalesConfig
from rest_framework.routers import SimpleRouter
from ads.views.comments import CommentViewSet

app_name = SalesConfig.name

router = SimpleRouter()
router.register('', CommentViewSet, basename='ad_comment')

urlpatterns = []

urlpatterns += router.urls
