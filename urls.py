from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
]