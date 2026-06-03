from django.shortcuts import render

def home(request):
    # Контекст для головної сторінки
    context = {
        'page_title': 'Головна - MotoGrand',
        'heading': 'Вітаємо в MotoGrand!',
        'content': 'Тут ви знайдете найкращі мотозапчастини.',
        'is_home': True  # Цей прапорець покаже список посилань
    }
    return render(request, 'shop/page.html', context)

def about(request):
    # Контекст для сторінки "Про нас"
    context = {
        'page_title': 'Про нас',
        'heading': 'Про компанію MotoGrand',
        'content': 'Ми продаємо запчастини для мотоциклів з 2026 року.',
        'is_home': False # Цей прапорець покаже кнопку "Назад"
    }
    return render(request, 'shop/page.html', context)

def catalog(request):
    # Контекст для сторінки каталогу
    context = {
        'page_title': 'Каталог',
        'heading': 'Наші товари',
        'content': 'Тут скоро будуть шоломи, шини та моторне масло.',
        'is_home': False
    }
    return render(request, 'shop/page.html', context)