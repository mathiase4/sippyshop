# SippyShop - Mug E-Commerce Store

- ![SippyShop mockup](screenshots/mockup.png)

## Live Project Link
- [Live Site on Heroku](https://sippyshop-project-249d59235c6d.herokuapp.com/)

## Table of Contents
- [Introduction](#introduction)
- [Project Purpose and Goals](#project-purpose-and-goals)
- [User Stories And Manuel Testing](#user-stories-and-manual-testing)
- [Agile Planning](#agile-planning)
- [Features](#features)
- [Future Features](#future-features)
- [Security](#security)
- [Accessibility](#accessibility)
- [Design Choices](#design-choices)
- [Automated Tests](#Automated-tests)
- [Validation](#validation)
- [ValidationscreenshotsHTML](#Validationscreenshotshtml)
- [ValidationscreenshotsCSS](#Validationscreenshotscss)
- [ValidationscreenshotsJS](#Validationscreenshotsjs)
- [ValidationscreenshotsFLAKE8](#Validationscreenshotsflake8)
- [Performance and Accessibility](#performanceandaccessibility)
- [Deployment](#deployment)
- [Wireframes](#wireframes)




## Introduction

SippyShop is a full-stack e-commerce web application built with Django. The idea is to have a small online store that sells mugs
where users can browse products, log in, add items to a cart, and place an order very easily. The project focuses on core webshop features rather
than a huge catalogue.
The app also supports user accounts so people can see their past orders and leave reviews on products they've bought, which makes the site a bit more interactive.

## Project Purpose and Goals

My main goal was to build a complete e-commerce site with Django that is so simple to use that
even a 6 year old can go in and look around on the website.

To plan the site, i broke it down into what a User (the customer) wants to do, and what (the site
owner) need to be able to do.

**User Goals**
- View a list of mugs and see product details
- Add products to the shopping cart
- Create an account and log in
- See order history
- Leave reviews on products

**Site Owner Goals**
- Sell products online
- Handle secure payments with (Stripe testmode)
- Manage products from the Django admin
- Keep users engaged through accounts and reviews




# User Stories And Manual Testing

### Must Have

- **View All Mugs** - Story: As a customer I want to see all mugs so I can choose what i want to buy
- Test: Go to /products/ and check all products are listed - **PASS**
  
  
- **Register Account** - **Story:** As a customer I want to register account so I can shop
- **Test:** Go to /accounts/signup/ (allauth) and create a new user - **PASS**
  

- **Login to see my orders** - **Story:** As a customer I want to login so I can see my orders
- **Test:** Go to /accounts/login/ and login with the user created above - **PASS**
  

- **Pay With Card** - **Story:** As a customer I want to pay with card so I can buy products
- **Test:** Add product to card and go to /checkout/ then submit stripe test payment - **PASS**
  
  
- **Payment Confirmation** - **Story:** As a customer I want to see confirmation after payment
- **Test:** After checkout the app redirects to payment_success - **PASS**
  
  
- **Add Product (Admin)** - **Story:** As an admin I want to add new products in admin panel
- **Test:** Login to /admin/ then products, add product - **PASS**
  
  
- **Edit Product (Admin)** - **Story:** As an admin I want to edit products when price change
- **Test:** In /admin/ edit and existing product - **PASS**
  
  
- **Delete Products (Admin)** - **Story:** As an admin I want to delete products when they are not available
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

# Validation

### HTML W3C Markup

- `accounts/templates/accounts - order_details.html (Removed unused <ul> and <li> now fixed - **PASS**
- `accounts/templates/accounts - order_history.html - **PASS**

- `products/templates/products - cart.html - **PASS**
- `products/templates/products - checkout.html - ( 1 Error from django-countries needs alt="") except from that **PASS**
- `products/templates/products - home.html - **PASS**
- `products/templates/products - product_detail.html - **PASS**
- `products/templates/products - product_list.html - **PASS**
- `products/templates/products - edit_review.html - **PASS**
- `products/templates/products - payment_success.html - **PASS** 
- `products/templates - base.html **PASS**

### CSS W3C Jigsaw

- `products/static/css - base.css - **PASS**
- `products/static/css - cart.css - **PASS**
- `products/static/css - checkout.css - **PASS**
- `products/static/css - payment_success.html - **PASS**
- `products/static/css - product_detail.html - **PASS**


### JavaScript JShint

- `products/statid/js - main.js (jshint didn't like const or let so i needed to change it to var to go through) - **PASS**
- `products/static/js - stripe-checkout.js ( want var so changed const to var, and everything was pass except import in comment that i use stripe) - **PASS**

### Flake8 - Python 

- To ensure the Python code follows PEP 8, the project was linted using flake8.
- .flake8 file was added in the project root:
- exclude = venv, .venv, env, migrations, __pycache__, manage.py.
- Run flake8 . in the terminal and everyting is clean.
  
  ### What was fixed with flake8
  
- removing trailing whitespace
- fixing extra/too many blank lines
- adding the required 2 blank lines before top-level defs/classes
- splitting overly long lines
- removing unused imports

## ValidationscreenshotsHTML


![home.html](screenshots/home.htmlvalidator.png)

![cart.html](screenshots/cart-html.validator.png)

![edit_review.html](screenshots/edit_review.htmlvalidator.png)

![payment_success.html](screenshots/payment_success.htmlvalidator.png)

![product_detail.html](screenshots/product_detail.htmlvalidator.png)

![product_list.html](screenshots/product_list.htmlvalidator.png)


## ValidationscreenshotsCSS


![base.css](screenshots/base.cssvalidator.png)

![cart.css](screenshots/cart.cssvalidator.png)

![checkout.css](screenshots/checkout.cssvalidator.png)

![payment_success.css](screenshots/payment_success.cssvalidator.png)

![product_detail.css](screenshots/product_detail.cssvalidator.png)


## ValidationscreenshotsJS


![main.js](screenshots/main.jsvalidator.png)

![stripe_checkout.js](screenshots/stripe-checkout.jsvalidator.png)


## ValidationscreenshotsFLAKE8


![flake8.test](screenshots/flake8validator.png)


## Performance and Accessibility

### Desktop Performance with Lighthouse
![Lighthousedesktop](screenshots/lighthousedesktop.png)

### Mobile Performance with Lighthouse
![Lighthousemobile](screenshots/lighthousemobile.png)

  
