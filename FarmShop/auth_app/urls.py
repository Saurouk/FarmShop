from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('contact/', views.contact_view, name='contact'),
]