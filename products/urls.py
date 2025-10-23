from django.urls import path
from . import views

# URL patterns for the products app
urlpatterns = [
    path('', views.product_list, name='product_list'),
]