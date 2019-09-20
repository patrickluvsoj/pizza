from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Login page")

def menu(request):
    return HttpResponse("Menu page")

def cart(request):
    return HttpResponse("Cart page")

def register(request):
    return HttpResponse("Sign-up page")
