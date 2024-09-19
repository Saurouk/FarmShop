# product/views.py
from rest_framework import viewsets
from .models import Product
from rest_framework import serializers


# Définition du sérialiseur pour le modèle Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Cela inclut tous les champs du modèle


# Définition du viewset pour le modèle Product
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
