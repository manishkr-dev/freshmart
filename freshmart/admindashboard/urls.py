from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('', views.homePage, name='home'),
    path('dashboard', views.adminPage, name='dashboard'),
    path('dashboard/addproduct', views.addProductPage, name='dashboard/addproduct'),
    
]