# product/models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)  # Champ pour la quantité disponible
    available = models.BooleanField(default=True)
    unit = models.CharField(max_length=50, default='kg')  # Nouveau champ pour l'unité

    def __str__(self):
        return self.name

    def is_in_stock(self):
        return self.quantity > 0
