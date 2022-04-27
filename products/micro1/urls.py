from micro1.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='micro1_product')
router.register(r'distributors', DistributorViewSet, basename='micro1_distributor')


urlpatterns = router.urls