from django.contrib import admin
import nested_admin
from cyberApp.models import Category, Type, Size, Product, ProductColor, ProductImage ,ContactUs,SectionImage,HeroImage

class ProductImageInline(nested_admin.NestedTabularInline):
    model = ProductImage
    extra = 1

class ProductColorInline(nested_admin.NestedStackedInline):
    model = ProductColor
    extra = 1
    inlines = [ProductImageInline]
    filter_horizontal = ['sizes']

class ProductAdmin(nested_admin.NestedModelAdmin):
    inlines = [ProductColorInline]
    list_display = ['name', 'category', 'product_type', 'price', 'is_featured']
    list_filter = ['category', 'product_type', 'is_featured']
    search_fields = ['name', 'description']


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')


class SectionImageAdmin(admin.ModelAdmin):
    list_display = ('section', 'created_at')

class HeroImageAdmin(admin.ModelAdmin):
    list_display = ('section', 'created_at')

admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Size)
admin.site.register(Product, ProductAdmin)
admin.site.register(ContactUs, ContactAdmin)
admin.site.register(SectionImage)
admin.site.register(HeroImage)


