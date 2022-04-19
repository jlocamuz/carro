from micro1.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'distributors', DistributorViewSet, basename='distributor')


urlpatterns = router.urls