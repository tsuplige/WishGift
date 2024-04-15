from django.db import models
from django.conf import settings


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    link = models.URLField()
    bought = models.BooleanField(default=False)
    buyerName = models.CharField(max_length=100, blank=True, null=True)
    # La relation avec la liste de souhaits est gérée par le modèle Wishlist

class Wishlist(models.Model):
    # La relation avec l'utilisateur propriétaire est gérée par le modèle User
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wishlist')
    items = models.ManyToManyField(Item)
