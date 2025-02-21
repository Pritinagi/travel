from django.db import models
from django.views.generic import ListView


# Create your models here.
#  models bnayenge , migration run krenge then migrations run krenge 
#  model define the database 

class contact(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    message = models.TextField(max_length=100)

class register(models.Model):
    fullname=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=10)


    
class adminreg(models.Model):
    username=models.CharField(max_length=15)
    password=models.CharField(max_length=50)

# # fetching user details
# class fetchuserdetails(ListView):
#     model = register
#     template_name = 'adminhome.html'
#     context_object_name = 'users'

# # fetching admin details
# class fetchadmindetails(ListView):
#     model = adminreg #table ka name
#     template_name = 'adminhome.html' # template - html page
#     context_object_name = 'admin' # obj from views - fetchadmindetails function


# class fetchmsg(ListView):
#     model = contact
#     template_name = 'adminhome.html'
#     context_object_name = 'msgs'

# product
class Product(models.Model):
    p_id=models.IntegerField()
    name = models.CharField(max_length=200)
    price = models.FloatField()
    duration = models.IntegerField()
    discount = models.IntegerField()

class cart1(models.Model):
    user=models.ForeignKey(register,on_delete=models.CASCADE)
    p_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    added_on=models.DateTimeField(auto_now_add=True)