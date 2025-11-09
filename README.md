# SippyShop  

## A e-commerce website for selling different type of mugs.

## Live Project Links

-**Live Site:**
-**Repository:**

## Table of Contents
- [Introduction](#introduction)
- [User Stories](#user-stories)
- [Agile Planning](#agile-planning)
- [Features](#features)
- [Future Features](#future-features)
- [Security](#security)
- [Accessibility](#accessibility)
- [Design Choices](#design-choices)
- [Automated Tests](#Automated-tests)
- [Manual Tests & Validation](#manual-tests&validation)
- [Deployment](#deployment)
- [Wireframes](#wireframes)


# User Stories And Manual Testing

### Must Have
- **View All Mugs** - Story: As a customer I want to see all mugs so I can choose what i want to buy
- Test: Go to /products/ and check all products are listed - **PASS**
  
- **Register Account** - **Story:** As a customer I want to register account so I can shop
- **Test:** Go to /accounts/signup/ (allauth) and create a new user - **PASS**

- **Login** - **Story:** As a customer I want to login so I can see my orders
- **Test:** Go to /accounts/login/ and login with the user created above - **PASS**

- **Pay With Card** - **Story:** As a customer I want to pay with cars so I can buy products
- **Test:** Add product to card and go to /checkout/ then submit stripe test payment - **PASS**
  
- **Payment Confirmation** - **Story:** As a customer I want to see confirmation after payment
- **Test:** After checkout the app redirects to payment_success - **PASS**
  
- **Add Product (Admin)** - **Story:** As a admin I want to add new products in admin panel
- **Test:** Login to /admin/ then products, add product - **PASS**
  
- **Edit Product (Admin)** - **Story:** As a admin I want to edit products when price change
- **Test:** In /admin/ edit and existing product - **PASS**
  
- **Delete Products** - **Story:** As a admin I want to delete products when they are not available
- **Test:** In /admin/ delete a product - **PASS**

- **Review Product** - **Story:** As a logged in customer I want to leave a review so I can tell others what I think
- **Test:** Go to product detail and submit review - **PASS**

- **Edit Review** - **Story:** As the review owner I want to edit my review so I can fix mistakes
- **Test:** Click "Edit" on own review - **PASS**

- **Delete Review** - **Story:** As the review owner I want to delete my review if I don't want it anymore
- **Test:** Click "Delete" on own review - **PASS**

# Automated Tests

## I made 5 automated tests to check that my models and views worked.
### Model Tests

- **test_create_product**: Test that a new product can be created.
- **test_create_order**: Test that a new order can be created(and fixed a bug where it needed a user).
- **test_create_review**: Test that a review can be created and linked to a product.
  
### View Tests

- **test_product_list_view**: Checks that the main shop page loads.
- **test_product_detail_view**: Checks that a single product's page loads.

### How to run tests?

1 - **Open the terminal**
2 - **Run this command** : Python3 manage.py test products

3 - **Results** : Ran 5 tests in 0.067s (OK)

### Should Have

- **Logout** - As a customer I want to logout from my account


### Could Have

- **Sort by Price** - As a customer I want to sort products by price
  
