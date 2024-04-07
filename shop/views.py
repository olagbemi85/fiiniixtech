from django.shortcuts import render, get_object_or_404
from .serializers import *
from rest_framework import generics
from rest_framework import mixins
from .models import *
from authentication.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.http import JsonResponse
import datetime
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import FormView


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
    product = get_object_or_404(Product, model=slug, in_stock=True)
    return render(request, './shop/products/detail.html', {'product': product})

'''
def search_view(request):
    if request.method == 'GET':
        form = SearchProductForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data.get('search_query', '')
            # Perform database search based on the search_query
            results = Product.objects.filter(title__icontains=search_query)
            return render(request, 'search_results.html', {'results': results, 'form': form})
    else:
        form = SearchProductForm()

    return render(request, 'search.html', {'form': form})
'''

# @login_required
def searchStation(request):
    #user = request.user
    #profile = User.objects.get(email=user)
    #pp= get_object_or_404(User, email=user)
    searchForm = SearchForm()
    query = request.GET.get('q')
    if query:
        results =   Product.objects.filter(product_type__icontains=query) | Product.objects.filter(capacity__icontains=query) | Product.objects.filter(model__icontains=query) | Product.objects.filter(name_of_manufaturer__icontains=query) | Product.objects.filter(category__name__icontains=query) #| Station.objects.filter(local_gov_area__icontains=query) 
    #elif query:
    #    Category.objects.filter(name__icontains=query)     
    else:
        results = Product.objects.none() 
    return render(request, './shop/products/search_result.html', {'query':query, 'results':results, 'searchForm':searchForm})


class ListViewProduct(ListView):
     model = Product
     template_name = './shop/products/product.html' 
     context_object_name = 'products'
     paginate_by = 6
     search_form =  SearchForm

     def get_queryset(self):
        queryset = Product.objects.all()
        search_query = self.request.GET.get('search_query')

        if search_query:
            queryset = Product.objects.filter(product_type__icontains=search_query) | Product.objects.filter(capacity__icontains=search_query) | Product.objects.filter(model__icontains=search_query) | Product.objects.filter(name_of_manufaturer__icontains=search_query)| Product.objects.filter(category__icontains=search_query) #| Station.objects.filter(local_gov_area__icontains=query)  )

        return queryset

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context