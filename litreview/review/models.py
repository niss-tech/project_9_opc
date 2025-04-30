from django.db import models
from django.contrib.auth.models import User
from tickets.models import Ticket


class Review(models.Model):
    """
    Modèle représentant une critique laissée par un utilisateur.

    Chaque critique est liée à un ticket existant.
    Elle contient une note, un titre (headline) et un commentaire (facultatif).

    Attributs :
        ticket (ForeignKey) : Le ticket auquel cette critique répond.
        rating (PositiveSmallIntegerField) : La note attribuée, entre 1 et 5.
        headline (CharField) : Le titre de la critique.
        body (TextField) : Le commentaire détaillé (facultatif).
        author (ForeignKey) : L'utilisateur qui a écrit la critique.
        time_created (DateTimeField) : Date et heure de création (automatique).
    """

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)]
    )
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Affiche une version lisible de la critique.
        """
        return f"Critique par {self.author} - {self.headline}"
