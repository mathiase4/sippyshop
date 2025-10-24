from django.shortcuts import render
from .models import Product


def home(request):
    """

Display homepage with hero section and all products.
    """
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products': products})


def product_list(request):
    """
    View to show all products,
    Shows all mugs available in the shop.
    """
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

