from django import forms


class FollowUserForm(forms.Form):
    """
    Formulaire permettant à un utilisateur
    de saisir le nom d’un autre utilisateur
    qu’il souhaite suivre.

    Args:
        username (CharField): Champ de texte
        pour entrer le nom d'utilisateur à suivre
        (max. 150 caractères).
    """
    username = forms.CharField(
        label="Nom d'utilisateur à suivre",
        max_length=150
    )
