from django.shortcuts import render

from django.http import HttpResponse

def home(request, param="Django"):
    return HttpResponse(f"<h1>Hello {param} !</h1>")

def contactUs(request):
    return HttpResponse("<h1>Contact Us !<h1>")

def aboutUs(request):
    return HttpResponse("<h1>About Us !<h1>")

