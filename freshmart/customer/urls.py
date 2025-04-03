from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name='home'),
    path('cart', views.cartPage, name='cart'),
    path('checkout', views.checkoutPage, name='checkout'),
    path('my-account', views.myaccountPage, name='my-account'),
    path('wishlist', views.wishlistPage, name='wishlist'),
    path('contact-us', views.contactPage, name='contact-us'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # path('firstpage', views.firstpage, name='firstpage'),
    path('categorypage/<int:id>', views.categorypage, name='categorypage'), 
    path('product-details', views.productdetailPage, name='product-details'),   
]