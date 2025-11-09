from django.test import TestCase
from django.urls import reverse
from .models import Product, Order, OrderItem, Review
from django-contrib.auth.models import User

class ModelTests(TestCase):
    def test_create_product(self):
        # test data configuration
        product = Product.objects.create(
            name="Test Mug",
            description="one test mug for coffee",
            price=99.99
        )
        
        self.assertEqual(product.name, "Test Mug") 
        self.assertEqual(product.price, 99.99)
        self.assertTrue(product.created_at)
        
    def test_create_review(self):
        # test create review linked to product/user
        user = User.objects.create(username="testuser")
        product = Product.objects.create(name="Test Mug", price=99.99)
        review = Review.objects.create(
            product=product,
            user=user,
            rating=5,
            comment="Great mug!"
        )
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.product.name, "Test Mug")
        
