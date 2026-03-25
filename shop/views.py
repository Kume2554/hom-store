from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
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
            messages.success(request, "เข้าสู่ระบบสำเร็จ!")
            return redirect('product_list')
        else:
            messages.error(request, "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
            return render(request, 'shop/login.html')
            
    return render(request, 'shop/login.html')

def logout_user(request):
    logout(request)
    messages.info(request, "ออกจากระบบเรียบร้อยแล้ว")
    return redirect('product_list')

def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    messages.success(request, f"เพิ่ม {product.name} ลงตะกร้าแล้ว (จำลอง)")
    return redirect('product_list')