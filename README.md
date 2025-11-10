# SippyShop - Mug E-Commerce Store

- ![SippyShop mockup](screenshots/mockup.png)

## Live Project Link
- [Live Site on Heroku](https://sippyshop-project-249d59235c6d.herokuapp.com/)

## Table of Contents
- [Introduction](#introduction)
- [Project Purpose and Goals](#project-purpose-and-goals)
- [Technologies Used](#technologies-used)
- [Django Apps](#django-apps)
- [Database and Models](#database-and-models)
- [User Authentication](#user-authentication)
- [User Stories And Manual Testing](#user-stories-and-manual-testing)
- [Features](#features)
- [Future Features](#future-features)
- [Security](#security)
- [JavaScript](#javascript)
- [Requirements](#requirements)
- [Attribution](#attribution)
- [Version Control](#version-control)
- [Design Choices](#design-choices)
- [Automated Tests](#automated-tests)
- [Validation](#validation)
- [ValidationscreenshotsHTML](#validationscreenshotshtml)
- [ValidationscreenshotsCSS](#validationscreenshotscss)
- [ValidationscreenshotsJS](#validationscreenshotsjs)
- [ValidationscreenshotsFLAKE8](#validationscreenshotsflake8)
- [Performance and Accessibility](#performance-and-accessibility)
- [Deployment](#deployment)
- [Wireframes](#wireframes)


## Introduction

SippyShop is a full-stack e-commerce web application built with Django. The idea is to have a small online store that sells mugs
where users can browse products, log in, add items to a cart, and place an order very easily. The project focuses on core webshop features rather
than a huge catalogue.
The app also supports user accounts so people can see their past orders and leave reviews on products they've bought.


## Project Purpose and Goals

My main goal was to build a complete e-commerce site with Django that is so simple to use that
even a 6 year old can look around on the website.

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


## Technologies Used

- HTML
- CSS
- JAVASCRIPT
- PYTHON & DJANGO
- POSTGRESQL
- STRIPE (TEST MODE ONLY)
- CLOUDINARY
- BOOTSTRAP (FOR LAYOUT AND DESIGN)
- DJANGO-ALLAUTH (FOR AUTHENTICATION)
- DJANGO-CRISPY-FORMS (FOR BETTER FORMS)


## Django Apps

This project has two main Django apps:
- **products:** Mug details,name,description,price,image,user registration, login, profiles.
- **accounts:** Order details,history detail,login_required.


## Database and Models
SippyShop uses a relational database (PostgreSQL)
**Custom Django models:**
- Product: Mug details (name, description,price, image)
- Order: Customer orders, linked to user, with delivery info and status
- OrderItem: Each product in an order, with quantity and price
- Review: Product reviews, linked to both product and user

The data schema is designed so that each order is linked to a user, each order
can have multiple items, and each review is linked to both a product and a user.

### Relationships:
- Each Order belongs to a User
- Each Order has many OrderItems
- Each OrderItem is linked to a Product
- Each Review belongs to a Product and a User


## User Authentication
- Users can register, login, and log out, using Django Allauth.
- Users must register to save their orders and write reviews.
- Only logged-in users can see their order history and write/edit/delete their own reviews.


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


# Features

Stripe is used for secure payments (test mode only),
All CRUD operations (Create, Read, Update, Delete) are supported for products and reviews.
Custom JavaScript is used for better user experience.

### Start Page
- The site has main navigation menu at the top of every page for easy access to all sections.
![herosection](screenshots/herosection.png)

### Product List
![productlist](screenshots/productlist.png)

### Product Detail and Review Section
![productdetail](screenshots/productdetail.png)

### Shopping Cart
![shoppingcart](screenshots/shoppingcart.png)

### Checkout
![checkout](screenshots/checkout.png)

### Payment Success!
![paymentsuccess](screenshots/paymentsuccess.png)

### User Account Features

- Signup
- Login
- Logout
- Forgot Password


## Future Features

- Add product categories (Sort by Price) are in githubs project sippyshop Todo/In Progress, Done.
- Add user profile page with address book.
- Add email automatic order notifications.


## JavaScript
Custom JavaScript is used for:
- Showing and hiding toast messages (notifications)
- Scroll-to-top buttom
- Mobile hamburger menu
- Product quantity (+/-) buttons
- Stripe payment form (handles card input, validation, and payment(testmode)

## Wireframes

### Start Page (Hero Section)
![WIREFRAMESTARTPAGE](screenshots/STARTPAGEWIREFRAME.png)

### Product List 
![WIREFRAMEPRODUCTLIST](screenshots/PRODUCTLISTWIREFRAME.png)

### Shopping Cart
![WIREFRAMESHOPPINGCART](screenshots/SHOPPINGCARTWIREFRAME.png)

### Checkout
![WIREFRAMECHECKOUT](screenshots/CHECKOUTWIREFRAME.png)


# Automated Tests
Both manual and automated tests have been done to make sure all main features work.

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


## Requirements
All Python dependencies are listed in requirements.txt
Main packages used:
- Django
- psycopg2-binary
- django-allauth
- stripe
- django-crispy-forms, crispy-bootstrap5
- cloudinary, django-cloudinary-storage
- django-countries
- gunicorn,whitenoise
- flake8

**Install with:**
`pip install -r requirements.txt`


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


## Design Choices


### Color Scheme
The site uses a dark, warm color inspired by autumn and coffee:
- **Background:** Darkbrown for a cozy coffee shop feel
- **Text:** cream/off-white for good readability
- **Accents:** Brown gradients for buttons and highlights

### Typography
- **Headings:** Merriweather gives a classic and elegant look
- **Body Text:** Montserrat for modern and easy to read

Both fonts are from Google Fonts

### Layout
- The site uses a simple, clean layout with clear sections
- Bootstrap grid system ensures the site is responsive on all devices
- Navigation meny collapses to hamburger menu on mobile screens
- Product cards use consistent spacing and hover effects

### Images
- All product images are square format for consistency
- Images are hosted on Cloudinary for fast loading
- Hero section uses a large background image to create visual impact


## Performance and Accessibility

The site has been tested with Lighthouse
for accessibility.

### Desktop Performance with Lighthouse
![Lighthousedesktop](screenshots/lighthousedesktop.png)

### Mobile Performance with Lighthouse
![Lighthousemobile](screenshots/lighthousemobile.png)


## Deployment 

This project uses a PostgreSQL database on Heroku and Cloudinary for all media file (image)
storage.
(Django DEBUG is set to False in production, and all secret keys are kept out of the codebase.)

### Deployment Steps

1. Push all code to Github.
2. Create a new app on Heroku.
3. Link the Github repository to the Heroku app for deployment.
4. Set all environment variables (Config Vars) in the Heroku app settings:
   - SECRET_KEY
   - DEBUG (set to False)
   - DATABASE_URL
   - CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET
   - STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY
     
5. Deploy the main branch from Github to Heroku
6. Run migrations to build the database: heroku run python3 manage.py migrate
7. Run collectstatic: heroku run python3 manage.py collectstatic

StaticFiles are handled bt WhiteNoise.
Images are stored with Cloudinary.

### Deployment Troubleshooting (Problems I Solved)
I ran into a few problems during deployment:
- **Problem 1: Product Images Disappeared**
- **Issue:** After deploying, all the product images were gone. The local database and
images did not transfer to Heroku.
- **Solution:** I had to first upload all my product pictures to Cloudinary.Then, I had to create a new
  admin account on the live site by running heroku run python3 manage.py createsuperuser.Finally, I had to log in
  to the Heroku admin panel and re-create all the products one by one, linkin them to the Cloudinary image URLs.

### Problem 2: Favicon Not Loading
- **Issue:** The small icon in the browser tab ( the favicon ) was not showing up.
- **Solution:** This was as simple spelling error. I had linked to favicon.png in my HTML, but the file
 was actually named Favicon.png(with a capital'F'). When i fixed the name in the HTML template, it loaded correctly.

### Problem 3: My Phone Got stolen So I Couldnt Login Into My Main Heroku Account
-**Issue:** Its true, my phone got stolen so i needed to buy a new one, but i had authenticator app for
Heroku on the old phone so had a big problem with connection my account and website deployment.
- **Solution:** Bought fast a new phone, tried to sign in but i couldnt cause of the authenticator app,
so i created a new heroku app, started over and bought the subscription i needed to use Heroku.


## Version Control

This project uses Git and Github for version control.
All code changes are tracked with regular commits.
Messages like: "Add models", "Add cart", "Add checkout", "Add Stripe test payment" and 
even some "Fix validators", or "added images to the library" "deployment setup" and problem fix.


## Security

- All secret keys ( sensitive information) and passwords are stored in environment variables,
  and are never commited to GitGub.
- .env file is in .gitignore and not uploaded to Github.
- Django DEBUG is set to False in production, and all secret keys are kept
  out of the codebase.
- Only allowed hosts can access the site.
- ALLOWED_HOSTS includes the Heroku domain
- CSRF_TRUSTED_ORIGINS includes the live URL
- Only staff can use Django admin
- users can only delete and edit their own reviews
- Order history is visible only to the owner


## Attribution
**Attribution:**
- All code is written by me unless otherwise stated.
  Any code from tutorials or other sources is marked with a comment and source link in the code and/or
  listed here in the README.

  - Used QuickRef.ME website for easy and quick cheatsheet in CSS and HTML/PYTHON
  - Used cssreference.io for help with box-shadow help with design the webiste
  - Used devdocs.io for more knowledge
  - Used w3schoools.com for most part CSS and Bootstrap, Django
  - Used Chatgpt for Guidance and explain stuff clearer so i understand fully in swedish
  - Used w3schools.com/howto/howto_js_scroll_to_top.asp
  - Used codewithharry.com for more guidance with Django coding and installing
  - Used Code institute cheatsheet django and videos, texts on the website
  - Used Stripe payment integration on the offical Stripe Django documentation, Code institute videos
  - Used Cloudinary setup followed with offical Cloudinary Django guide.
  - Used Django allauth setup followed this Youtube tutorial used settings.py help:[https://www.youtube.com/watch?v=qqFCt0Yde40]
  - Used PostgreSQL code from Code Institute my 3 key used
  - Used this Youtube tutorial video for more django knowledge while coding along:[https://www.youtube.com/watch?v=0gAFW4UxsZg&list=PL4cUxeGkcC9iqfAag3a_BKEX1N43uJutw]
  - Used this Youtube tutorial video for a remainder and knowledge to create the scrollUpButton with js:[https://www.youtube.com/watch?v=nw7I1vfOzzw]
 







  
