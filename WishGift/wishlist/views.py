from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Wishlist, Item
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Item  # Assurez-vous que le modèle est correctement importé
from .forms import ItemForm  # Créez un formulaire pour WishlistItem si nécessaire


@require_POST
def add_item(request):
    form = ItemForm(request.POST)
    if form.is_valid():
        # Enregistrez le nouvel item sans lui associer de wishlist pour l'instant
        item = form.save(commit=False)
        item.user = request.user  # Associe l'item à l'utilisateur qui l'a créé
        item.save()

        # Ensuite, associez l'item à la wishlist de l'utilisateur
        request.user.wishlist.add_item(item)
        return redirect('home')  # Redirige vers la page de wishlist après l'ajout
    return render(request, 'wishlist/home.html', {'form': form})  # Réaffichez le formulaire avec erreurs si invalide


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


@login_required
def item_delete(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        if request.user == item.user or request.user.is_superuser:
            item.delete()
            return redirect('home')
        return redirect('home')

    return redirect('home')
