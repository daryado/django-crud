from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Вернет текст "Hello World"
def index(request):
    return HttpResponse('Hello World')

# Вернет текст "About"
def about(request):
    return HttpResponse('About')