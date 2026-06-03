from django.contrib import admin
from .models import Category, Brand, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Виводимо колонки: назва, створено, оновлено
    list_display = ('name', 'created_at', 'updated_at')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Тут виводимо ще й зв'язані поля (бренд, категорію, ціну)
    list_display = ('name', 'category', 'brand', 'price', 'created_at', 'updated_at')