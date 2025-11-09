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


# User Stories

### Must Have
- **View All Mugs** - As a customer I want to see all mugs so I can choose what i want to buy
- **Register Account** - As a customer I want to register account so I can shop
- **Login** - As a customer I want to login so I can see my orders
- **Pay With Card** - As a customer I want to pay with cars so I can buy products
- **Payment Confirmation** - As a customer I want to see confirmation after payment
- **Add Product** - As a admin I want to add new products in admin panel
- **Edit Product** - As a admin I want to edit products when price change
- **Delete Products** - As a admin I want to delete products when they are not available

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
  
