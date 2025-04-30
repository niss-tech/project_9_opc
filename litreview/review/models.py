from django.db import models
from django.contrib.auth.models import User
from tickets.models import Ticket


class Review(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)]
    )
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Critique par {self.author} - {self.headline}"
