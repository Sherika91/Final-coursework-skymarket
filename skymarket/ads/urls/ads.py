from rest_framework.routers import SimpleRouter
from ads.views.ads import AdViewSet
from ads.apps import SalesConfig

app_name = SalesConfig.name

router = SimpleRouter()
router.register('', AdViewSet, basename='ads')

urlpatterns = []

urlpatterns += router.urls
