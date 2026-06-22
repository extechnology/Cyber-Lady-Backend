from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    product_type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    is_featured = models.BooleanField(default=False)
    material = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProductColor(models.Model):
    product = models.ForeignKey(Product, related_name='colors', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, help_text="e.g. Midnight Black")
    color_code = models.CharField(max_length=20, help_text="Hex code e.g. #000000")
    sizes = models.ManyToManyField(Size, related_name='available_colors')

    def __str__(self):
        return f"{self.product.name} - {self.name}"

class ProductImage(models.Model):
    product_color = models.ForeignKey(ProductColor, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.product_color.name} ({self.product_color.product.name})"



SECTION_CHOICES = (
    ('stats', 'STATS'),
)

class SectionImage(models.Model):
    section = models.CharField(max_length=20, choices=SECTION_CHOICES, unique=True)
    image = models.ImageField(upload_to='sections/')
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.section


class HeroImage(models.Model):
    image = models.ImageField(upload_to='hero/')
    alt_text = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title or f"Hero Image {self.id}"


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"