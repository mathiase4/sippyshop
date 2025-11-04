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


def product_detail(request, product_id):
    """
    View to show individual product details."""
    product = Product.objects.get(id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})


def add_to_cart(request, product_id):
    """
    Add product to shopping cart.
    """
    product = Product.objects.get(id=product_id)
    cart = request.session.get('cart', {})
    
    # Get quantity from form (default 1)
    quantity = int(request.POST.get('quantity', 1))
    
    # if product already in cart, increase quantity
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += quantity
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': str(product.price),
            'quantity': quantity,
            'image': product.image.url if product.image else None
        }
        
    # save cart to session
    request.session['cart'] = cart
    request.session.modified = True
    
    #Redirect back to product detail
    return redirect('product_detail', product_id=product_id)

def view_cart(request):
    """
    display shopping cart.
    """
    cart = request.session.get('cart', {})
    
    # calculate total
    total = 0
    for item in cart.values():
        total += float(item['price']) * item['quantity']
        
    content = {
        'cart': cart,
        'total': total
    }
    return render(request, 'products/cart.html', context)

def update_cart(request, product_id):
    """
    Update product quantity in cart.
    """
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity', 1))
    
    if str(product_id) in cart:
        if quantity > 0:
            cart[str(product_id)]['quantity'] = quantity
        else:
            del cart[str(product_id)]
            
    request.session['cart'] = cart
    request.session.modified = True
    
    return redirect('view_cart')

def remove_from_cart(request, product_id):
    """
    Remove product from cart.
    """
    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        del cart[str(product_id)]
        
    request.session['cart'] = cart
    request.session.modified = True
    
    return redirect('view_cart')
    
