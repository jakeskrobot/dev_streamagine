from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post

class FinderPageView(ListView):
    model = Post
    template_name = 'finder.html'
    context_object_name = 'all_posts_list'

class FinderDetailView(DetailView):
    model = Post
    template_name = 'finder_detail.html'

class FinderNewView(CreateView):
    model = Post
    template_name = 'finder_new.html'
    fields = ['title', 'author', 'body']

class FinderEditView(UpdateView):
    model = Post
    template_name = 'finder_edit.html'
    fields = ['title', 'body']

class FinderDeleteView(DeleteView):
    model = Post
    template_name = 'finder_delete.html'
    success_url = reverse_lazy('finder:home')

