from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1> Student IT Services - Home </h1>')

def about(request):
    return HttpResponse('<h1> Student IT Services - About us </h1>')

def contact(request):
    return HttpResponse('<h1> Student IT Services - Contact us </h1>')

def product(request):
    return HttpResponse('<h1> Student IT Services - products page </h1>')