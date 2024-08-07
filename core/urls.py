from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact, name='contact'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    path('detail/', views.detail, name='detail'),
    path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),
    path('base/', views.base, name='base'),


    ]