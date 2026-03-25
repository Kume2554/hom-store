from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def login_user(request):
    return render(request, 'shop/login.html' , {})

def logout_user(request):
    return render(request, 'shop/logout.html' , {})