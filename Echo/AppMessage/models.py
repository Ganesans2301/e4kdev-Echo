
from django.db import models

class Message(models.Model):
    # This model is just a placeholder and doesn't need fields
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
