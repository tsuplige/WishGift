from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Wishlist, Item


@login_required
def index(request):
    wishlist = Wishlist.objects.get_or_create(owner=request.user)[0]
    items = wishlist.items.all()

    return render(request, 'wishlist/home.html', {'wishlist': wishlist,
                                                  'items': items})


@login_required
def friendlist(request):
    return render(request, 'wishlist/friendlist.html')


@login_required
def friendwishlist(request):
    return render(request, 'wishlist/friendwishlist.html')
