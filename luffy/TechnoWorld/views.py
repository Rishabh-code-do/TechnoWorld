from django.shortcuts import render
from django.http import HttpResponse
from .models import content,category

# Create your views here.

def index(request):
    conts = content.objects.all()
    return render(request, 'index.html',{'conts':conts})

def why(request):
    return render(request, 'why.html')

def about(request):
    return render(request, 'about.html')

def product(request):
    cats=category.objects.all()

    conts = content.objects.all()
    return render(request,'product.html',{'conts':conts,'cats':cats})



