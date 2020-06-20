from django.http import HttpResponse
from django.shortcuts import render
from . models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def james(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})



def stephen(request):
    return HttpResponse("Hello")