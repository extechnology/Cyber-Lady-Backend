from rest_framework import viewsets
from cyberApp.models import *
from cyberApp.serializers import *

# product & category related viewsets

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class SizeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer

class ProductColorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductColor.objects.all()
    serializer_class = ProductColorSerializer

class ProductImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

# section images viewset

class SectionImagesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SectionImage.objects.all()
    serializer_class = SectionImagesSerializer


# contact viewset  

class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactSerializer