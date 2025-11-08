from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.conf import settings
import stripe 
from .models import Product, Order, OrderItem, Review
from .forms import OrderForm, ReviewForm
from allauth.account.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetFromKeyView,
    PasswordResetFromKeyDoneView,
)


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
    View to show individual product 
    details and handles review form submissions.
    """
    product = get_object_or_404(Product, id=product_id)
    
    reviews = product.reviews.all().order_by('-created_at')
    
    # review code 
    review_form = ReviewForm()
    
    if request.method == 'POST':
        
        
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to leave a review.')
            return redirect('account_login')
        
        review_form = ReviewForm(data=request.POST)
        
        if review_form.is_valid():
            
            try:
                Review.objects.get(user=request.user, product=product)
                messages.error(request, 'You have already reviewed this product.')
                
            except Review.DoesNotExist:
                
                review = review_form.save(commit=False)
                
                # add user and product
                review.user = request.user
                review.product = product
                
                review.save() # save 
                messages.success(request, 'Your review has been submitted!')
                
            return redirect('product_detail', product_id=product.id)
        
        else:
            messages.error(request, 'Please correct the errors in the form.')
            
    
    context = {
        'product': product,
        'reviews': reviews,
        'review_form': review_form,
    }
    return render(request, 'products/product_detail.html', context)
        
       
    


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
   if cart is empty after removal , go to cart
   else go back to the page we came from (cart or checkout)
    """
    cart = request.session.get('cart', {})
    product_id = str(product_id)
    
    if product_id in cart:
        product = Product.objects.get(id=product_id)
        del cart[product_id]
        messages.success(request, f'{product.name} removed!')
        
    
    request.session['cart'] = cart
    request.session.modified = True
    
    # if cart goes empty
    if not cart:
        return redirect('view_cart')
    
    referer = request.META.get('HTTP_REFERER', '')
    
    if 'cart' in referer:
        return redirect('view_cart')
    
    # come from checkout
    if 'checkout' in referer:
        return redirect('checkout')
    
   # fallback
    return redirect('view_cart')
    
    
def checkout(request):
    """
    Display checkout page with Stripe Payment.
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
        
        
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            #create order
            order = form.save(commit=False)
            order.user = request.user if request.user.is_authenticated else None 
            order.total_amount = total
            
            # create stripe payment here
            stripe.api_key = settings.STRIPE_SECRET_KEY
            
            try:
                intent = stripe.PaymentIntent.create(
                    amount=int(total * 100), # stripe uses cents
                    currency=settings.STRIPE_CURRENCY,
                    metadata={'order_id': order.id}
                )
                
                order.stripe_payment_intent = intent.id 
                order.save()
                
                # Save order items 
                for item in cart_items:
                    OrderItem.objects.create(
                        order=order,
                        product=item['product'],
                        quantity=item['quantity'],
                        price=item['product'].price
                    )
                    
                    # clear cart
                request.session['cart'] = {}
                    
                messages.success(request, ' Order placed successfully!')
                return redirect('payment_success', order_id=order.id)
                
            except stripe.error.StripeError as e:
                messages.error(request, f'x Payment error: {str(e)}')
                
    else:
        form = OrderForm()
            
            
    context = {
            'cart_items': cart_items,
            'total': total,
            'form': form,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        }
        
    return render(request, 'products/checkout.html', context)

def payment_success(request, order_id):
    """
    Display payment success page
    """
    try:
        order = Order.objects.get(id=order_id)
        context = {'order': order}
        return render(request, 'products/payment_success.html', context)
    except Order.DoesNotExist:
        messages.error(request, 'Order not found')
        return redirect('product_list')
    
    
def payment_cancel(request):
    """
    Display payment cancelled page
    """
    messages.warning(request, 'Payment was cancelled')
    return redirect('view_cart')

        # ================ DJANGO PASSWORD RESET =================

class MyPasswordResetView(PasswordResetView):
    template_name = 'account/password_reset.html'
        
    
class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'
    
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "check your email for the reset link.")
        return super().dispatch(request, *args, **kwargs)
    
    
class MyPasswordResetFromKeyView(PasswordResetFromKeyView):
    template_name = 'account/password_reset_form_key.html'
    
    def form_valid(self, form):
        messages.success(self.request, "Your password has ben changed.")
        return super().form_valid(form)
    
    
class MyPasswordResetFromKeyDoneView(PasswordResetFromKeyDoneView):
    template_name = 'account/password_reset_from_key_done.html'
    
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Password reset is complete.")
        return super().dispatch(request, *args, **kwargs)
        