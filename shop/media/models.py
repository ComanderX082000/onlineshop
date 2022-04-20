from tabnanny import verbose
from django.db import models
from datetime import datetime,timezone
from django.conf import settings
from django.utils.text import slugify


class Category(models.Model):
    class Meta:
        verbose_name="Kategoriya"
        verbose_name_plural="Kategoryalar"
    name = models.CharField(max_length=256,verbose_name="Nomi")
    icon = models.ImageField(upload_to="images/",verbose_name="Rasm")
    slug = models.CharField(max_length=256,null=True)

    def __str__(self):
        return self.name
class SubCategory(models.Model):
    verbose_name='Kichik Kategorya'
    verbose_name_plural="Kichik Kategoryalar"

    name = models.CharField(max_length=256, verbose_name="Nomi")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.CharField(max_length=256,null=True)
    def __str__(self):
        return self.name

class SubSubCategory(models.Model):
    name = models.CharField(max_length=256, verbose_name="Nomi")
    category = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    slug = models.CharField(max_length=256,null=True)
    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=256, verbose_name="Nomi")
    category = models.ForeignKey(SubSubCategory,on_delete=models.CASCADE)
    slug = models.CharField(max_length=256,null=True)
    def __str__(self):
        return self.name

class ProductColor(models.Model):
    name = models.CharField(max_length=256)


    def __str__(self):
        return self.name

class Productsize(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name

   

class Product(models.Model):
    class Meta:
        verbose_name="Mahsulot"
        verbose_name_plural="Mahsulotlar"
    

    title = models.CharField(max_length=256)
    price = models.FloatField()
    slug =models.SlugField(default='',editable=False)
    description = models.TextField()
    rating = models.FloatField()
    image = models.ImageField(upload_to="images/")
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    color = models.ManyToManyField(ProductColor,related_name='products')
    size = models.ManyToManyField(Productsize,related_name='products')
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.price}"
    

    def get_rating_percent(self):
        return 100 * (self.rating / 5)
    

    def is_new_product(self):
        time_delta = datetime.now(timezone.utc) - self.created_at
        return time_delta.seconds < settings.NEW_PRODUCT_SECONDS
    
class Variations(models.Model):
    product_id=models.IntegerField()
    name=models.CharField(max_length=255)
    slug=models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class ProductImage(models.Model):
    image = models.ImageField(upload_to="images/", )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")




        









