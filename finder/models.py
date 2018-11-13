from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
from accounts.models import *

class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    body = models.TextField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('finder:finder_detail', args=[str(self.id)])

class Comment(models.Model):
    article = models.ForeignKey(Post, on_delete=models.CASCADE, related_name ='comments')
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse('finder:home')
