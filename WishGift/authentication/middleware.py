from django.http import HttpResponseRedirect
from django.urls import reverse


class RedirectToHomeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:  # Vérifie si l'utilisateur est connecté
            if request.path == '/':  # Vérifie si l'URL est la racine
                return HttpResponseRedirect(reverse('home'))  # Redirige vers la page d'accueil
        return self.get_response(request)