from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    """
    Modèle représentant une demande de critique (ticket).

    Ce modèle est utilisé lorsqu'un utilisateur souhaite
    demander une critique sur un livre, un film ou tout autre contenu.

    Attributs :
        title (CharField): Le titre de la demande (obligatoire).
        description (TextField): Une description plus détaillée
            du contenu à critiquer (facultatif).
        image (ImageField): Une image associée à la demande (facultatif).
        user (ForeignKey): L'utilisateur qui a créé ce ticket.
        time_created (DateTimeField): La date et l'heure de création
            du ticket (ajoutée automatiquement).
    """

    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='ticket_images/'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Affiche le titre du ticket dans l'administration ou en console.
        """
        return f"Ticket : {self.title}"
