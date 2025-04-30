from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm


def signup_view(request):
    """
    Gère l'inscription d'un nouvel utilisateur.

    Args:
        request (HttpRequest): Requête HTTP contenant
        les données du formulaire.

    Returns:
        HttpResponse: Redirection vers le feed ou réaffichage du formulaire.
    """
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('feed')
    return render(
        request,
        'authentication/signup.html',
        {'form': form}
    )


def landing_view(request):
    """
    Affiche la page d'accueil avec le formulaire de connexion.

    Args:
        request (HttpRequest): Requête HTTP.

    Returns:
        HttpResponse: Page de connexion (landing).
    """
    form = AuthenticationForm()
    return render(
        request,
        'authentication/landing.html',
        {'form': form}
    )
