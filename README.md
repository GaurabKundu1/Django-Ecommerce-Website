# Django-Ecommerce-Store

An Eccomerce Store Made with HTML, CSS, JAVASCRIPT, BOOTSTRAP, PYTHON and DJANGO.

Users can register themselves, login to their accounts, add products to cart, checkout and pay.


Payment Gate way succesfully integrated (Using Paypal).

Customized Django Administration pannel for Admins.

2 coupons are applicable, codeclouds10 for 10 % discount on shopping >= $100, codeclouds20 for 20% discount on shopping >= $200.


This is how the Store looks like



https://github.com/CodeClouds-Gaurab/Django-Ecommerce-Store/assets/154874892/329d1dd4-5afd-4b54-886d-2652d248eeb1


Register new user

![Screenshot (2)](https://github.com/CodeClouds-Gaurab/Django-Ecommerce-Store/assets/154874892/dc4f18d2-e276-407d-bb9e-7521eebbad0c)


Fill all the details about the user and click register,


![Screenshot (3)](https://github.com/CodeClouds-Gaurab/Django-Ecommerce-Store/assets/154874892/88abf829-7318-48e3-8cb3-c90a35d39135)


It will take you to Sign in page


![Screenshot (4)](https://github.com/CodeClouds-Gaurab/Django-Ecommerce-Store/assets/154874892/96c7ca8f-d010-4786-8922-aebc6ac30bd6)

Enter your username and password then click Login.

Now add some products to your cart


![Screenshot (5)](https://github.com/CodeClouds-Gaurab/Django-Ecommerce-Store/assets/154874892/1014b9fd-134c-4663-afe4-c9c6b34dfd3f)


The Subtotal is now $ 165.94 as its < $200 & > $100 we can use coupon code codeclouds10 to get a 10 % discount

After Applying the coupon the subtotal is now $ 149.35

![Screenshot (6)](https://github.com/CodeClouds-Gaurab/Django-Ecommerce-Store/assets/154874892/051fec31-7eae-4d2c-8b7c-33f63167527b)

Now click on checkout fill all the details and click continue


![Screenshot (7)](https://github.com/CodeClouds-Gaurab/Django-Ecommerce-Store/assets/154874892/ccdf5968-0a6f-4952-8d22-0b2cf37385ca)


We will be paying using Paypal

![Screenshot (8)](https://github.com/CodeClouds-Gaurab/Django-Ecommerce-Store/assets/154874892/0be92af1-756e-4f1e-b153-9f372ebb26fa)


Click on complete purchase and your purchase will be done

![Screenshot (9)](https://github.com/CodeClouds-Gaurab/Django-Ecommerce-Store/assets/154874892/8dd6e083-bb64-4f55-8748-67a30ecad3aa)


![Screenshot (10)](https://github.com/CodeClouds-Gaurab/Django-Ecommerce-Store/assets/154874892/68e1bf50-51ce-47e0-af19-4f526e8b0aef)

You will be able to see your order details

![Screenshot (11)](https://github.com/CodeClouds-Gaurab/Django-Ecommerce-Store/assets/154874892/6ec52a66-a994-4c5c-b1b8-c1a6fec6f1ad)

Click on the eye icon to see your ordered products

![Screenshot (12)](https://github.com/CodeClouds-Gaurab/Django-Ecommerce-Store/assets/154874892/1a39c392-99c1-4f49-9ed8-df60100fb1f6)


Admin Pannel

![Screenshot (13)](https://github.com/CodeClouds-Gaurab/Django-Ecommerce-Store/assets/154874892/172bae43-40bd-4c0f-b2e1-3076fd50625d)

Enter your Admin credentials and login


![Screenshot (14)](https://github.com/CodeClouds-Gaurab/Django-Ecommerce-Store/assets/154874892/9126ff8f-52ca-4196-8456-7fc59faf6574)

Go to orders and you will find all the orders that has been placed so far

![Screenshot (15)](https://github.com/CodeClouds-Gaurab/Django-Ecommerce-Store/assets/154874892/5dee6e35-a7a9-4c15-8e01-a5248d4f0e39)

Click on any one and you will be able to see the complete details including transaction id and paypal transaction id

How to get started?

on your terminal type git clone https://github.com/CodeClouds-Gaurab/Django-Ecommerce-Store.git

Go to this repository in your machine and open in terminal,

now type python -m venv env 

this will create a virtual environment

activate it and then in the same terminal

type pip install -r requirements.txt

once all the dependencies are installed run the command python manage.py runserver

Access the app at http://127.0.0.1:8000/

