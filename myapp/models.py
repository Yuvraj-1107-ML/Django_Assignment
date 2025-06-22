# api/models.py

from django.db import models
from django.contrib.auth.models import User

class TelegramUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_username = models.CharField(max_length=255)

    def __str__(self):
        return self.telegram_username
