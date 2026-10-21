from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hello,Welcome to the shop home page!")
def products(request):
    return HttpResponse("This is the products page of the shop.")