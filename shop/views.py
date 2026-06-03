from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def home(request):
    # Витягуємо ВСІ товари і ВСІ категорії з бази
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'page_title': 'Головна - MotoGrand',
        'products': products,
        'categories': categories,
    }
    return render(request, 'shop/home.html', context)


def category_view(request, category_id):
    # Витягуємо товари тільки конкретної категорії
    categories = Category.objects.all()  # Потрібно для меню
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)

    context = {
        'page_title': f'Категорія: {category.name}',
        'products': products,
        'categories': categories,
        'current_category': category,
    }
    return render(request, 'shop/home.html', context)


def about(request):
    categories = Category.objects.all()
    return render(request, 'shop/about.html', {'page_title': 'Про нас', 'categories': categories})