"""
URL configuration for travel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from homeapp import views

# first visit to urls.travel pr
# 2nd urls.homeapp pr 
# agr match hua tou show krega thik vrna nhi 

urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('contact',views.Contact, name='contact'),
    path('login',views.login, name='login'),
    path('destination',views.destination, name='destination'),
    path('register',views.registration, name='registration'),
    path('blog',views.blog, name='blog'),
    path('home',views.home, name='home'),
    # run views.index wala function
    path('cart',views.cart, name='cart'),
    path('rajasthan',views.rajasthan, name='rajasthan'),
    path('gujrat',views.gujrat, name='gujrat'),
    path('goa',views.goa, name='goa'),
    path('jammu',views.jammu, name='jammu'),
    path('varansi',views.varanasi, name='varanasi'),
    path('jaipur',views.jaipur,name='jaipur'),
    path('adminlogin',views.adminlogin, name='adminlogin'),
    path('adminreg',views.adminreg1, name='adminreg'),
    
    # path('adminhome',views.product, name='adminhome' ), ye work out nahi kr rha 

    path('adminhome',views.fetchuserdetails, name='adminhome' ),
    # In simple terms, when a user visits /adminhome, Django will call the fetchuserdetails function from views.py and render the associated template (adminhome.html).
    # path('adminhome', views.fetchadmindetails, name='adminhome'),
    path('aa/',views.des2),
    path('sikkim',views.sikkim,name='sikkim'),
    path('kashmir',views.kashmir, name='kashmir.html'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart,name='add_to_cart')
]