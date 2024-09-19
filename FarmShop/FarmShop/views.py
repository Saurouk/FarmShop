from django.shortcuts import render, redirect
from django.contrib import messages



def home_view(request):
    return render(request,'home.html')

def blog_view(request):
    return render(request,'blog.html')

def product_view(request):
    return render(request,'product.html')




