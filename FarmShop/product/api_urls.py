from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# Créez un routeur et enregistrez les vues du produit
router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
