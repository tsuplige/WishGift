from . import forms
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = forms.LoginForm()
        message = ''
        if request.method == 'POST':
            form = forms.LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                )
                if user is not None:
                    login(request, user)
                    return redirect('home')
            message = 'Identifiants invalides.'
        return render(request, 'authentication/login.html', context={
            'form': form, 'message': message})


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    return render(request, 'authentication/signup.html',
                  context={'form': form})


def logout_user(request):

    logout(request)
    return redirect('login')
