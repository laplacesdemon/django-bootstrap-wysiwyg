from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
