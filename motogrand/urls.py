from django.contrib import admin
from django.urls import path, include # Додали include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')), # Підключили посилання нашого додатку
]