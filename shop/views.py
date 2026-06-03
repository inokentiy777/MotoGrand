from django.shortcuts import render, get_object_or_404
from .models import Product, Category


# Це для сторінки категорії (щоб було видно тільки товари цієї категорії)
def category_view(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)  # ФІЛЬТРАЦІЯ

    return render(request, 'shop/home.html', {
        'products': products,
        'categories': categories,
        'current_category': category
    })


# Це для сторінки конкретного товару
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()

    return render(request, 'shop/product.html', {
        'product': product,
        'categories': categories
    })