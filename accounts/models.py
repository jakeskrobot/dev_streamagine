from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    twitch_username = models.CharField(max_length=128,)

    def get_absolute_url(self):
        return reverse('accounts:my_account')


