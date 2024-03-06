

from django.shortcuts import render, get_object_or_404
from .serializers import ServiceSerializer
from rest_framework import generics
from rest_framework import mixins
from .models import *
from authentication.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.http import JsonResponse
import datetime
from django.urls import reverse
from shop.models import Category, Product


@login_required
def special(request):
    return HttpResponse("You are logged in !")


def home(request):
    pc = Category.objects.all()
    products = Product.objects.all().order_by('-updated')#[:3]
    context = {
        "pc": pc,
        "products": products
    }            
    return render(request, './home.html', context)

def contact_us(request):
    if request.method == 'POST':
        username = request.POST('username')
        first_name = request.POST('firstname')
        last_name = request.POST('lastname')
        address = request.POST('address')
        email = request.POST('email')
        subject = request.POST('subject')
        subject_description =  request.POST('description')
        phone_number = request.POST('phone')
        contacts = Contact.object.create_user(username,first_name,last_name,address,email,subject,subject_description,phone_number)
        contacts.save()
    else:
        return render(request, './mainpage/form/contact_us.html', {})    
        #return render(request, 'form/contact_us.html')


def slideshows_terms(request):
    docues = SlideShowM.objects.all()
    return render(request, './mainpage/terms.html', {'docues': docues})


def all_slideshows(request):
    docu = SlideShowM.objects.all()
    return render(request, './mainpage/policies.html', {'docu': docu})


def slideshows_about(request):
    docus = SlideShowM.objects.all()
    return render(request, './mainpage/about.html', {'docus': docus})



# services section
def all_service(request):
    servs = Service.objects.all()
    return render(request, './mainpage/services/all_service.html', {'servs': servs})


def serviceCategory_list(request, category_slug=None):
    sercategory = get_object_or_404(ServiceCategory, slug=category_slug)
    services = Service.objects.filter(sercategory=sercategory)
    return render(request, './mainpage/services/category.html', {'sercategory': sercategory, 'services': services})


def service_detail(request, slug):
    service= get_object_or_404(Service, slug=slug, in_stock=True)
    return render(request, './mainpage/services/detail.html', {'service': service})

def load_inverter_calu_services(request):
    
    return render(request, './mainpage/services/load_inverter_calcu.html')
#services section end


class ServiceGenericAPIView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    lookup_field = 'id'

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id =None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

