from django.shortcuts import render
from django.views.generic import ListView

from .models import Post

class FinderPageView(ListView):
    model = Post
    template_name = 'finder.html'
    context_object_name = 'all_posts_list'
