from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Formulaire de création ou modification d'une critique.

    Ce formulaire est basé sur le modèle Review et permet
    à l'utilisateur de créer une critique pour un ticket donné.

    Args:
        ticket (ForeignKey): Le ticket auquel la critique est liée.
        rating (PositiveSmallIntegerField): La note de 1 à 5.
        headline (CharField): Le titre de la critique.
        body (TextField): Le contenu de la critique.

    Widgets:
        rating (RadioSelect): Affichage des notes sous forme de boutons radio,
        avec des choix allant de 1 à 5.
    """
    class Meta:
        model = Review
        fields = ['ticket', 'rating', 'headline', 'body']
        widgets = {
            'rating': forms.RadioSelect(
                choices=[(i, str(i)) for i in range(1, 6)]
            ),
        }
