from django.urls import path
from . import views

# URL patterns for the products app
urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
]