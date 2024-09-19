from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from .models import Product

class ProductListCreate(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer