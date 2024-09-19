from django.shortcuts import render
from django.http import HttpResponse

def user_view(request):
    return render(request,'users/user_list.html')

def create_view(request):
    return HttpResponse("Page de création d'utilisateur")