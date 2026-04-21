from django.shortcuts import render
from .models import Product

# Функция, которая отвечает за страницу со списком товаров
def product_list(request):
  #получаем все товары из базы
  products = Product.objects.all() #взять все товары

  # Передаём их в шаблон
  return render(request, 'products/product_list.html', { #render(...) → отрисовать HTML страницу
              'products': products #'products': products → передать данные в шаблон
              })