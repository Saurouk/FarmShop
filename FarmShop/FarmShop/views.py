from django.http import HttpResponse


def home_view(requet):
    return HttpResponse("Hello World")