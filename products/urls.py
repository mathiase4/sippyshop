from django.urls import path
from . import views

# URL patterns for the products app

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('bag/add/<int:pk>/', views.add_to_bag, name='add_to_bag'),
]