from micro1.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'client', ClientDetailViewSet, basename='client')
router.register(r'shopping_cart', ShoppingCartViewSet, basename='shopping_cart')
router.register(r'cart_detail', CartDetailViewSet, basename='cart_detail')
router.register(r'sale', SaleViewSet, basename='sale')
router.register(r'sale_detail', SaleDetailViewSet, basename='sale_detail')
urlpatterns = router.urls