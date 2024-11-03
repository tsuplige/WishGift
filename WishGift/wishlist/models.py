from django.db import models
from django.conf import settings


class Item(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='have_create', blank=True, null=True)
    description = models.TextField()
    price = models.FloatField(blank=True, null=True)
    link = models.URLField(blank=True, null=True, max_length=500)
    bought = models.BooleanField(default=False)
    buyer = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
        related_name='have_buy', blank=True, null=True)

    def mark_as_bought(self):
        self.bought = True
        self.save()

    def set_buyer(self, user):
        self.buyerName = user
        self.save()


class Wishlist(models.Model):

    owner = models.OneToOneField(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name='wishlist')
    items = models.ManyToManyField(Item, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def add_item(self, item):
        if not self.items.filter(pk=item.pk).exists():
            self.items.add(item)

    def remove_item(self, item):
        if self.items.filter(pk=item.pk).exists():
            self.items.remove(item)
