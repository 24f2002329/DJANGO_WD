from django.http import HttpResponse
from django.shortcuts import render     # importing request and render from django.shortcuts

def index(request):
    # return HttpResponse("Hello World")
    return render(request, 'website/index.html')    # importing request and render from django.shortcuts

def about(request):
    return render(request, 'website/about.html')   

def contact(request):
    return render(request, 'website/contact.html')


