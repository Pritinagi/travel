from django.shortcuts import render , HttpResponse, get_object_or_404,redirect
from homeapp.models import contact
from homeapp.models import register
from homeapp.models import adminreg
from homeapp.models import Product


# from .forms import ContactForm 
# Create your views here.

def index(request):
    # to send  a variable 
    # context = {
    #     "variable1": "this is sent",
    #     "variable2": "this is sent"
    # }
    # context set of variables  which are send to templates, it is a python dictionary 
    #  render ke sath 3 chezein share hui hai context , template and variable
    # used to fetch value from modals and then send further to template by creating variable
    # return render(request, 'index.html',context)
    return render(request, 'index.html')
    # return HttpResponse("this is home page")
    # directly string ko render krne ke liye httpresponse use krte h
def home(request):
    # return render(request, 'about.html')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("this is about page")
     return render(request, 'about.html')
# we have to mention here where the recieved  data should be stored 



def Contact(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Create and save a new contact instance
        new_contact = contact(firstname=firstname, lastname=lastname, phone=phone, email=email, message=message)
        new_contact.save()
        return render(request, 'contact.html', {'success': True})  # Optionally pass a success flag to the template
    return render(request, 'contact.html')

# return render(request, 'contact.html')



def login(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        password= request.POST['password']
        user=register.objects.filter(fullname=fullname , password=password)
        if user:
            return render(request, 'home.html')
        else:
            return render(request, 'login.html', {'error': 'Wrong information'})
    return render(request, 'login.html')



# remove this 
def aa(request):
    if request.method == 'POST ':
        fullname= request.POST['fullname']
        password= request.POST['password']
        user = register.objects.filter(fullname=fullname, password = password)
        if user : 
            return render(request, ' home.html')
        else:
            return render (request, 'ogin.html', {'error' : 'wrong information'})

def destination(request):
    # return HttpResponse("this is destination page")
    return render(request, 'destination.html')

def blog(request):
    return render(request, 'blog.html')

def registration(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname', '').strip()  # Strip removes leading/trailing spaces
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        if register.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already exists!'})
        if len(password) < 8:
            return render(request, 'register.html', {'error': 'Password must be at least 8 to 10 characters long!'})
        # Create and save a new register instance
        new_register = register(fullname=fullname, email=email, password=password)
        new_register.save()
        return render(request, 'home.html', {'success': True})
    return render(request, 'register.html')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def fetchuserdetails(request):
    
    if request.method == 'POST':
      
        # Extract data from the POST request
        # if request.POST['submit1']
        # sub_button=request.POST['submit1']
        # del_button=request.POST['delete1']
        # up_button=request.POST['update1']
        print(request.POST.get('delete1'))
        if request.POST.get('delete1'):
            print("clicked")
        else:
            print("not")
        return redirect("adminhome")
        # if request.POST.get('delete1'):
        #     print("yes")
        # else:
        #     print("no")
        # p_id = request.POST['p_id']
        # name = request.POST['name']
        # price = request.POST['price']
        # duration = request.POST['duration']
        # discount = request.POST['discount']
        # # Create a new Product instance
        # new_product = Product( p_id=p_id, name=name, price=price, duration=duration, discount=discount)
        # # Save the product to the database
        # new_product.save()

        

    user = register.objects.all()  # Fetch all records from the database
    adminuser = adminreg.objects.all()
    msg = contact.objects.all()
    productlist = Product.objects.all()
    # return render(request, 'adminhome.html', {'user': adminhome})
    print("hello ")
    return render(request, 'adminhome.html', {'list1': user,'list2' : adminuser, 'list3' : msg , 'list4' :productlist })
# render(): Renders the template with the request and context.
# 'adminhome.html': The template that will cdbe rendered.
# {'list1': user}: The context data, where list1 is the name you can use in the template, and user is the actual data passed to it.
# to fetch more then 1 table in a page we will use dictionary method and will create only one function for it .


from.models import cart1
def add_to_cart(request,product_id):
    product= get_object_or_404(Product,p_id=product_id)
    cart_item,created=cart1.objects.get_or_create(user=register.firstname,p_id=product_id)
    if not created:
        cart_item.save()
    # yuvi7858794@gmail.com
    # Yugesh@123

def cart(request):
    # return HttpResponse("this is cart page")

    return render(request, 'cart.html')
def rajasthan(request):
    # return HttpResponse("this is cart page")
    return render(request, 'rajasthan.html')
def gujrat(request):
    # return HttpResponse("this is cart page")
    return render(request, 'gujrat.html')
def jammu(request):
    # return HttpResponse("this is cart page")
    return render(request, 'jammu.html')
def goa(request):
    # return HttpResponse("this is cart page")
    return render(request, 'goa.html')

def varanasi(request):
    return render(request, 'varanasi.html')

def jaipur(request):
    data=Product.objects.filter(p_id=101)
    return render(request, 'jaipur.html',{'data':data})


def sikkim(request):
    return render(request, 'sikkim.html')

def kashmir(request):
    return render(request, 'kashmir.html')

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password= request.POST['password']
        user=adminreg.objects.filter(username=username, password=password)
        if user:
            return render(request, 'home.html')
        else:
            return render(request, 'adminlogin.html', {'error': 'Wrong information'})
    return render(request, 'adminlogin.html')

# function name and model name should not be same to prevent from errors 
def adminreg1(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()  # Strip removes leading/trailing spaces
       
        password = request.POST.get('password', '').strip()
        if adminreg.objects.filter(username=username).exists():
            # adminreg is model name
            return render(request, 'adminreg.html', {'error': 'USERNAME already exists!'})
        if len(password) < 8 and len(password)>=10:
            return render(request, 'adminreg.html', {'error': 'Password must be at least 8 to 10 characters long!'})
        # Create and save a new register instance
        new_register = adminreg(username=username,password=password)
        new_register.save()
        return render(request, 'home.html', {'success': True})
    return render(request, 'adminreg.html')


def adminhome(request):
    return render (request, 'adminhome.html')


def des2(request):
    return render(request,'des2.html')



# product add
# def product(request):
#     if request.method =='POST':
#         name= request.POST['name']
#         p_id = request.POST['p_id']

# def product(request):
#     if request.method == 'POST':
#         # Extract data from the POST request
#         p_id = request.POST['p_id']
#         name = request.POST['name']
#         price = request.POST['price']
#         duration = request.POST['duration']
#         discount = request.POST['discount']
#         # Create a new Product instance
#         new_product = Product( p_id=p_id, name=name, price=price, duration=duration, discount=discount)
#         # Save the product to the database
#         new_product.save()
#         return render(request, 'adminhome.html',{'success' : True})  # Redirect or render a success page
#     return render(request, 'adminhome.html')  # Render the form for GET requests

