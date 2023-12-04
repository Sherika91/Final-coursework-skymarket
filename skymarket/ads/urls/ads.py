from django.urls import path, include
from rest_framework.routers import SimpleRouter
from ads.views.ads import AdViewSet, UserAdsAPIView
from ads.apps import SalesConfig

app_name = SalesConfig.name

router = SimpleRouter()
router.register('', AdViewSet, basename='ads')

urlpatterns = [
    path('me/', UserAdsAPIView.as_view(), name="User-ads"),

]

urlpatterns += router.urls
