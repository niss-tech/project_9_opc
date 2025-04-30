from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
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
        return f"Ticket : {self.title}"
