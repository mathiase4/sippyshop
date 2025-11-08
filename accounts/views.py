from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from products.models import Order

@login_required
def order_history(request):
    """
    show history list on orders for users. (login required)
    """
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'orders': orders
    }
    return render(request, 'accounts/order_history.html', context)


@login_required
def order_detail(request, order_id):
    """
    show details on specific orders.
    """
    
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    context = {
        'order': order
    }
    return render(request, 'accounts/order_detail.html', context)
