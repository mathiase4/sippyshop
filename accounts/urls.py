from django.urls import path
from . import views

urlpatterns = [
    # main site for order history
    path('history/', views.order_history, name='order_history'),

    # detail site for orders
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
]
