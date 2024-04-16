from django.contrib import admin
from .models import Wishlist, Item


@admin.register(Item)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')


@admin.register(Wishlist)
class UserFollowAdmin(admin.ModelAdmin):
    list_display = ('owner', 'created')

