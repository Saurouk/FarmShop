from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

path('', views.user_view, name ='user'),
path('create/', views.create_view),

]


