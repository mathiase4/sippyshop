from django.test import TestCase
from django.urls import reverse
from .models import Product, Order, OrderItem, Review
from django.contrib.auth.models import User

class ModelTests(TestCase):
    def test_create_product(self):
        # test data configuration
        product = Product.objects.create(
            name="Test Mug",
            description="one test mug for coffee",
            price=99.99,
            image="path/to/test.jpg"
        )
        
        self.assertEqual(product.name, "Test Mug") 
        self.assertEqual(product.price, 99.99)
        self.assertTrue(product.created_at)
        
    def test_create_order(self):
        # test create and check an order
        user = User.objects.create(username="testuser_order")
        
        order = Order.objects.create(
            user=user,
            full_name="Test User",
            email="test@example.com",
            total_amount=99.99,
            status="pending"
        )
        self.assertEqual(order.full_name, "Test User")
        self.assertEqual(order.total_amount, 99.99)
        
    def test_create_review(self):
        # test create review linked to product/user
        user = User.objects.create(username="testuser")
        product = Product.objects.create(
            name="Test Mug",
            price=99.99,
            image="path/to/test.jpg"
        )
        
        review = Review.objects.create(
            product=product,
            user=user,
            rating=5,
            comment="Great mug!"
        )
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.product.name, "Test Mug")
        
class ViewTests(TestCase):
    def test_product_list_view(self):
        # test if product list view loads Ok
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        
    def test_product_detail_view(self):
        # test to create product and check detail page
        product = Product.objects.create(
            name="Test Mug",
            price=99.99,
            image="path/to/test.jpg"
        )
        response = self.client.get(reverse('product_detail', args=[product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Mug")