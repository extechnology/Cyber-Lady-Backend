from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cyberApp.views import (
    CategoryViewSet, TypeViewSet, SizeViewSet,
    ProductViewSet, ProductColorViewSet, ProductImageViewSet,
    ContactViewSet,SectionImagesViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'types', TypeViewSet)
router.register(r'sizes', SizeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-colors', ProductColorViewSet)
router.register(r'product-images', ProductImageViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'section-images', SectionImagesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
