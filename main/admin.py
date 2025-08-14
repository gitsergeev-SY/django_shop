from django.contrib import admin
from .models import Category, Product
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name', 'slug']
  prepopulated_fields = {'slug': ('name',)}

@admin.register(Product) 
class ProductAdmin(admin.ModelAdmin):
  list_display = ['name', 'category', 'slug', 'image', 'price', 'description', 'available', 'created_at', 'updated_at']
  list_filter = ['available', 'created_at', 'updated_at', 'category']
  list_editable = ['available', 'price']
  prepopulated_fields = {'slug': ('name',)}
