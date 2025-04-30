from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    """
    Formulaire pour créer ou modifier un ticket.

    Ce formulaire est basé sur le modèle Ticket et permet
    à l'utilisateur de demander une critique pour un livre
    ou un article, en fournissant un titre, une description
    et une image optionnelle.

    Args:
        title (CharField): Le titre du ticket (obligatoire).
        description (TextField): La description du contenu
        à critiquer (optionnelle).
        image (ImageField): Une image illustrant le contenu (optionnelle).
    """
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
