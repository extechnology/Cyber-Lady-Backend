from cyberApp.models import ContactUs
from rest_framework import serializers
from cyberApp.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text']

class ProductColorSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    sizes = SizeSerializer(many=True, read_only=True)

    class Meta:
        model = ProductColor
        fields = ['id', 'name', 'color_code', 'sizes', 'images']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    product_type = TypeSerializer(read_only=True)
    colors = ProductColorSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'category', 'product_type', 'price', 
            'description', 'is_featured', 'material', 'colors', 
            'created_at', 'updated_at'
        ]



class SectionImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionImage
        fields = ['id', 'image', 'alt_text', 'section', 'created_at', 'updated_at']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id', 'name', 'email', 'subject', 'message', 'created_at']