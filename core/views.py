from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def shop(request):
    return render(request, 'shop.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def contact(request):
    return render(request, 'contact.html')


def detail(request):
    return render(request, 'detail.html')


def base(request):
    return render(request, 'base.html')


def login(request):
    return render(request, 'login.html')
