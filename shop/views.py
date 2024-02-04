from django.shortcuts import render, get_object_or_404
from .serializers import *
from rest_framework import generics
from rest_framework import mixins
from .models import *
from authentication.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
#from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.http import JsonResponse
import datetime
from django.urls import reverse


def all_products(request):
    pc = Category.objects.all()
    products = Product.objects.all().order_by('-updated')#[:3]
    context = {
        "pc": pc,
        "products": products
    }            
    return render(request, './shop/products/product.html', context)


def category_list(request, slug=None):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, './shop/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, './shop/products/detail.html', {'product': product})
