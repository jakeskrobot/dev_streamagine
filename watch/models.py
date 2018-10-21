from django.db import models
from django.urls import reverse
from accounts.models import *

class Stream(models.Model):
    stream_name = models.CharField(max_length=200)
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE,)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('finder:finder_detail', args=[str(self.id)])
