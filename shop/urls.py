from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_view, name='category'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    # Нові шляхи для Лаби 7:
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('subscribe/', views.subscribe_newsletter, name='subscribe'),
]