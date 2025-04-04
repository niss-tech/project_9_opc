from django.db import models

# Create your models here.
# listings/models.py

class Band(models.Model):
    name = models.fields.CharField(max_length=100)