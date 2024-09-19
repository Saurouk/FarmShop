
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name ='home'),
    path('blog/', views.blog_view,name ='blog'),
    path('product/', include('product.urls')),
    path('api/', include('product.urls')),
    path('auth_app/', include('auth_app.urls')),
    path('user/', include('user.urls')),


]
