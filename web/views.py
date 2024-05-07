from django.shortcuts import render
from product.models import Product

def home(request):
    products = Product.objects.all()
    print(products)
    return render(request,'web/home.html',{'products':products})