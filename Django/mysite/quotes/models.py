from django.db import models

# Create your models here.
class Quotes(models.Model):
    text: models.TextField()
    author: models.CharField(max_length=100)
