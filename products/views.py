from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
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
    
    # show message
    messages.success(request, f'{product.name} added to cart!')
    
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
        
    context = {
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
        product = Product.objects.get(id=product_id)
        del cart[str(product_id)]
        messages.success(request, f'{product.name} removed!')
        

    request.session['cart'] = cart
    request.session.modified = True
    
    return redirect('view_cart')
    
    
def checkout(request):
    """
    Display checkout page with order form.
    """
    cart = request.session.get('cart', {})
    
    # Redirect if cart is empty
    if not cart:
        messages.warning(request, 'Your cart is empty!')
        return redirect('product_list')
    # Calculate cart items and total
    
    cart_items = []
    total = 0
    
    for product_id, item_data in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            quantity = item_data['quantity']
            item_total = float(item_data['price']) * quantity
            total += item_total
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total
            })
        except Product.DoesNotExist:
            continue
        
    context = {
            'cart_items': cart_items,
            'total': total,
    }
        
    return render(request, 'products/checkout.html', context)
