from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
   name = models.CharField(max_length=100, db_index=True)
   slug = models.SlugField(max_length=100, unique=True)

   def __str__(self):
       return self.name
   
   class Meta:
      ordering = ['name',]
      verbose_name = 'category'
      verbose_name_plural = 'categories'

   def get_absolute_url(self):
       return reverse("main:product_list_by_category", args=[self.slug])
      

class Product(models.Model):
   category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
   name = models.CharField(max_length=100, db_index=True)
   slug = models.SlugField(max_length=100, unique=True)
   image = models.ImageField(upload_to='products/%Y/%m/%d')
   price = models.DecimalField(max_digits=20, decimal_places=2)
   description = models.TextField(blank=True)
   available = models.BooleanField(default=True)
   created_at = models.DateTimeField(auto_now_add=True, null=True) 
   updated_at = models.DateTimeField(auto_now=True)
   
   class Meta:
      ordering = ['name',] 
    
   def __str__(self):
       return self.name
   
   def get_absolute_url(self):
       return reverse("main:product_detail", args=[self.id ,self.slug])
 
   