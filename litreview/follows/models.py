from django.db import models
from django.contrib.auth.models import User


class UserFollows(models.Model):
    """
    Modèle représentant une relation de suivi entre deux utilisateurs.

    Ce modèle permet à un utilisateur (user) de suivre
    un autre utilisateur (followed_user).

    Attributs :
        user (ForeignKey) : L'utilisateur qui suit quelqu'un.
        followed_user (ForeignKey) : L'utilisateur qui est suivi.

    Contraintes :
        unique_together : Empêche qu’un même utilisateur
        suive deux fois la même personne.
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )
    followed_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followers'
    )

    class Meta:
        unique_together = ('user', 'followed_user')

    def __str__(self):
        """
        Retourne une phrase lisible décrivant la relation de suivi.
        """
        return f"{self.user.username} suit {self.followed_user.username}"
