from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('order',views.order,name='order'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path('login',views.loginuser,name="login"),
    path('logout',views.logoutuser,name="logout"),
    path('signup',views.signupview,name="signup"),

]
