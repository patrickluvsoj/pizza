from django.http import HttpResponse
from django.shortcuts import render
from .models import Order, Product, SubT, PizzaT

# Create your views here.
def index(request):
    return HttpResponse("Login page")

def menu(request):
    return render(request, 'menu.html')

def submenu(request, category):
    return HttpResponse(category)

def cart(request):
    cart = Order.date
    print(Order.products)

    return HttpResponse(f'You have ordered: {cart}')

def register(request):
    return HttpResponse("Sign-up page")


# TODO
#1 SPA
#   hello.html
#   download sample projects from course
#   make simple SPA
#   enable HTML history
#   dice3.html use handle bars to  enable actual forms


#2 Auth
#   setup login and registratgion page
#   setup authenticaiton using Django
#   check out users project for Django


#3 DB  
#   Setup DB model
    # ensure  pricing is facotored into the equation
#   Hook-up form w/ DB model
#   Show raw results in a page



#4 Carts
#   Create cart page
#   Quesry products in cart
#   Enable subnit order and store order history

#5 History
#   Setup order histopry  page
#   Create order details from  history (re-use cart page?)

#6 Update cart
#   Enable update/delete cart
#   Add animation for deleting products

#7 Additional features
#   Add SMS
#   Enable Stripe