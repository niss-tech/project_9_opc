from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    """
    Formulaire personnalisé pour l'inscription
    d'un nouvel utilisateur.

    Args:
        email (EmailField): Champ requis pour
        l’adresse e-mail de l’utilisateur.

    Meta:
        model (User): Modèle utilisateur fourni par Django.
        fields (list): Champs affichés dans le formulaire :
            - username : nom d’utilisateur.
            - email : adresse email.
            - password1 : mot de passe.
            - password2 : confirmation du mot de passe.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
