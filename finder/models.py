from django.db import models
from django.urls import reverse
from accounts.models import *

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('finder:finder_detail', args=[str(self.id)])
