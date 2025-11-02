from django.shortcuts import render, get_object_or_404, redirect
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


def product_detail(request, pk):
    """
    View to show individual product details."""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})


def add_to_bag(request, pk):
    """
    add a product to the shopping bag."""
    if request.method == 'POST':
        bag = request.session.get('bag', {})
        key = str(pk)
        bag[key] = bag.get(key, 0) + 1
        request.session['bag'] = bag
        return redirect(request.META.get('HTTP_REFERER', 'products_list'))