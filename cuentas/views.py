from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request): 
    return HttpResponse('Home page')

def medicamentos(request):
    return HttpResponse('Contact page')

def usuario(request):
    return HttpResponse('Contact page')