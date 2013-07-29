from django.db import models
from django.core.urlresolvers import reverse


class Message(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()

    def get_absolute_url(self):
        return reverse("demo:message-update", args=[self.pk])
