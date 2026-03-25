from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def login_user(request):
    return render(request, 'shop/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('product_list')

def cart_add(request, product_id):
    return redirect('product_list')