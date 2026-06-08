from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from decimal import Decimal
from .models import Product, Category, Newsletter, Review
from .forms import ReviewForm


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'shop/home.html', {'products': products, 'categories': categories})


def category_view(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'shop/home.html',
                  {'products': products, 'categories': categories, 'current_category': category})


# --- ЛАБА 7: СТОРІНКА ТОВАРУ ТА ВІДГУКИ ---
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()

    # Обробка форми відгуку
    if request.method == 'POST' and 'review_submit' in request.POST:
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.user = request.user
                review.save()
                messages.success(request, "Ваш відгук успішно додано!")
                return redirect('product_detail', product_id=product.id)
        else:
            messages.error(request, "Щоб залишити відгук, потрібно увійти в систему.")

    review_form = ReviewForm()

    return render(request, 'shop/product.html', {
        'product': product,
        'categories': categories,
        'review_form': review_form,
    })


# --- ЛАБА 7: КОШИК ---
def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = Decimal('0.00')

    for prod_id, item_data in cart.items():
        product = get_object_or_404(Product, id=prod_id)
        total_item_price = Decimal(item_data['price']) * item_data['quantity']
        total_price += total_item_price
        cart_items.append({'product': product, 'quantity': item_data['quantity'], 'total': total_item_price})

    categories = Category.objects.all()
    return render(request, 'shop/cart.html',
                  {'cart_items': cart_items, 'total_price': total_price, 'categories': categories})


def add_to_cart(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        product = get_object_or_404(Product, id=product_id)
        quantity = int(request.POST.get('quantity', 1))

        prod_id_str = str(product.id)
        if prod_id_str in cart:
            cart[prod_id_str]['quantity'] += quantity
        else:
            cart[prod_id_str] = {'price': str(product.price), 'quantity': quantity}

        request.session['cart'] = cart
        messages.success(request, f"{product.name} додано до кошика!")
    return redirect('cart_detail')


# --- ЛАБА 7: РОЗСИЛКА ---
def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            Newsletter.objects.get_or_create(email=email)
            messages.success(request, "Дякуємо за підписку на наші новини!")
    return redirect(request.META.get('HTTP_REFERER', 'home'))