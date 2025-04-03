from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from . models import *
from admindashboard.models import Customer, product, StateChoicesTag
from django.shortcuts import render, get_object_or_404


def categorypage(request, id):
    cat = get_object_or_404(product, id=id)
    prod = product.objects.filter(product_category=cat.product_category)

    # Fetch tagged products
    new_arrival_tag, _ = StateChoicesTag.objects.get_or_create(state=product.StateChoices.NEW_PRODUCT_ARRIVALS)
    trending_tag, _ = StateChoicesTag.objects.get_or_create(state=product.StateChoices.TRENDING_PRODUCT)
    recent_tag, _ = StateChoicesTag.objects.get_or_create(state=product.StateChoices.RECENT_PRODUCT)

    new_arrivals = product.objects.filter(product_state=new_arrival_tag)
    trending_products = product.objects.filter(product_state=trending_tag)
    recent_products = product.objects.filter(product_state=recent_tag)

    return render(request, 'categorypage.html', {
        'cat': cat,
        'prod': prod,
        'new_arrivals': new_arrivals,
        'trending_products': trending_products,
        'recent_products': recent_products,
    })

def homePage(request):
    prod = product.objects.all() 
    new_arrival_tag, _ = StateChoicesTag.objects.get_or_create(state=product.StateChoices.NEW_PRODUCT_ARRIVALS)
    featured_tag, _ = StateChoicesTag.objects.get_or_create(state=product.StateChoices.FEATURED_PRODUCT)
    trending_tag, _ = StateChoicesTag.objects.get_or_create(state=product.StateChoices.TRENDING_PRODUCT)
    recent_tag, _ = StateChoicesTag.objects.get_or_create(state=product.StateChoices.RECENT_PRODUCT)

    # Fetch products based on tags
    prod = product.objects.all()
    new_arrivals = product.objects.filter(product_state=new_arrival_tag)
    trending_products = product.objects.filter(product_state=trending_tag)
    recent_products = product.objects.filter(product_state=recent_tag)
    featured_products = product.objects.filter(product_state=featured_tag)

    # Render the template with filtered products
    return render(request, 'index.html', {
        'prod': prod,
        'new_arrivals': new_arrivals,
        'trending_products': trending_products,
        'recent_products': recent_products,
        'featured_products': featured_products
    })

def cartPage(request):
    return render(request, "cart.html")
def checkoutPage(request):
    return render(request, "checkout.html")
def myaccountPage(request):
    return render(request, "my-account.html")
def contactPage(request):
    return render(request, "contact-us.html")
def wishlistPage(request):
    return render(request, "wishlist.html")
def productdetailPage(request):
    return render(request, "product-detail.html")

def register(request):
    if request.method == "POST":
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        # img=request.POST[' img']
        mobile=request.POST['mobile']
        # address=request.POST['address']
        
        Customer.objects.create(name=name,username=username, email=email, password=password, mobile=mobile,  ) #address=address,
        return redirect('home')
    return render (request, 'index.html')
        
def login(request):
    if request.method == "POST":
        username=request.POST['username']
        # email=request.POST['email']
        password=request.POST['password']
        # phone=request.POST['phone']
        cust=Customer.objects.filter(username=username, password=password).first() # mobile=phone The filter will return multiple data from the database
        # cust=Customer.objects.get(id=5) the get return only single data from database
        if cust is not None:
            request.session['id']=cust.id
            request.session['name']=cust.name
            request.session['username']=cust.username
            request.session['password']=cust.password
          
          # mail sending
          
            subject=("Thank you for login")
            message = f"Hi {cust.name}, Thank you for login"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [cust.email, ]
            send_mail(subject, message, email_from, recipient_list )
            
            messages.info(request, 'Login Successful')
            redirect('home')
        else:
            messages.info(request, 'Login Failed')
            redirect('login')
        #     return HttpResponse('LOgin Successful')
        # else:
        #     return HttpResponse('Login Failed')
        
    return render (request, 'index.html')



def logout(request):
    del request.session['id']
    del request.session['name']
    del request.session['email']
    del request.session['phone']