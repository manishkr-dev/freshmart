from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def adminPage(request):
    return render(request, "admin-dashbord.html")
def addProductPage(request):
    return render(request, "addproduct.html")

# def home(request):
#     return HttpResponse("Hello World")