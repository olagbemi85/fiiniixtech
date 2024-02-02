

from django.shortcuts import render, get_object_or_404
#from .serializers import ServiceSerializer
from rest_framework import generics
from rest_framework import mixins
from .models import *
from django.views import View
from django.db.models.signals import post_save
#from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, UserFormUpdate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.core import serializers
from django.http import JsonResponse
import datetime
from django.urls import reverse
from django.contrib import messages
from .signals import *


@login_required
def special(request):
    return HttpResponse("You are logged in !")


        
class LoginView(View):
	def get(self, request):
		if request.user.is_authenticated:
			return redirect('mainpage:home')
		else:
			return render(request, 'authentications/forms/login.html')

	def post(self, request):	
			email = request.POST['email']
			password = request.POST['password']
			
			if email and password:
				user = authenticate(email=email, password=password)
				if user:
					if user.is_active:
						login(request, user)
						messages.success(request, 'Welcome,'+ user.username+'you are now logged in')
						return redirect('mainpage:home')
					messages.error(request, 'Account is not active')
					return render(request, 'authentications/forms/login.html')
				messages.error(request, 'Invalide credentials')
				return render(request, 'authentications/forms/login.html')
			messages.error(request, 'Please fill all fields')					
			return render(request, 'authentications/forms/login.html')

class LogoutView(View):
	def get(self, request):
		logout(request)
		messages.success(request, 'logout')
		return redirect('mainpage:home')


class Reg(View):
	user_form = UserForm()
	def get(self, request, data=None):
		if request.user.is_authenticated:
			return redirect('mainpage:home')
		else:
			messages.success(request, 'Please fill in your data')
			context = {'form': self.user_form}
			return render(request, 'authentications/forms/register.html', context) 
	
	def post(self, request):
		if request.method == 'POST':
			#user_form = UserForm(data=request.POST)
			user_form = UserForm(request.POST)
			username = request.POST['username']
			first_name = request.POST['first_name']
			last_name = request.POST['last_name']
			email = request.POST['email']
			password = request.POST['password']
			err = {'form' :user_form}

			context = {
				'username':username, 'email':email, 'first_name':first_name, 'last_name':last_name, 'password':password,
				}
			if user_form.is_valid():
				if not User.objects.filter(username = username).exists():
					if not User.objects.filter(email = email).exists():
						if len(password) < 8:
							messages.error(request, 'password too short')
							return render(request, 'authentications/forms/register.html', err)
                        
						user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name)
						#create_user_profile()
						user.save()
						user.set_password(password)
						user.save()
						#save_user_profile()

						messages.success(request, 'Account successfully created')
						return redirect('authentication:userlogin')                         
					messages.error(request, 'e-mail taken')
					return render(request, 'authentications/forms/register.html', err)
				messages.error(request, 'user exist')
				return render(request, 'authentications/forms/register.html', err)
			return render(request, 'authentications/forms/register.html', err)
			#return self.get(request, msg)



@login_required
def profile(request):
    user = request.user
    post = User.objects.get(email=user) # This query object give logged in user profile
    context = {'post' : post}
    return render(request, 'authentications/profile-detail.html', context)	


@login_required
def profile_customer(request):
    user = request.user
    pp = User.objects.get(email=user)
    if request.method == 'POST':
        user_form = UserFormUpdate(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('authentication:edit-profile')
        else:
            messages.error(request, 'fail to save profile')
    else:
       	#try:
            user_form = UserFormUpdate(instance=request.user)
        #except:
            #profile = User.objects.create(user=request.user)
            #user_form = UserFormUpdate(instance=profile)
    return render(request, 'authentications/forms/update_profile.html', {'user_form': user_form, 'pp':pp })



