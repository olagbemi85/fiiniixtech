
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


app_name = 'authentication'


urlpatterns = [
    path('edit-profile/', profile_customer, name='edit-profile'),
    path('user_login', LoginView.as_view(), name='userlogin'),
    path('profile/', profile, name='profile'),
    path('register/', Reg.as_view(), name='register'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

]
