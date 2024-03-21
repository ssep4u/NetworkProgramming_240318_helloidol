from django.http import HttpResponse
from django.shortcuts import render

def say_hello(request):
    return HttpResponse("Hello World")

def say_hello_html(request):
    return render(request, 'playground/hello.html')