from django.shortcuts import render
from . models import product
# Create your views here.

def product(request):
    return render(request,'products/product.html')

def products(request):
    return render(request, 'products/products.html', {'pro':product.objects.all()})
