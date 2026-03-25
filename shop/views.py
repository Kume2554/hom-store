from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def login_user(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            return render(request, 'shop/login.html', {'error': 'Invalid login'})
    return render(request, 'shop/login.html')

def logout_user(request):
    logout(request)
    return redirect('product_list')

def cart_add(request, product_id):
    # ฟังก์ชันชั่วคราวกันปุ่มพัง
    return redirect('product_list')