from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'unit', 'quantity', 'available')  # Inclure quantity ici
    list_filter = ('available',)  # Filtres disponibles dans la colonne latérale
    search_fields = ('name', 'description')  # Champs sur lesquels rechercher

    # Configuration des champs du formulaire d'édition
    fields = ('name', 'description', 'price', 'unit', 'quantity', 'available')  # Inclure quantity ici

admin.site.register(Product, ProductAdmin)
