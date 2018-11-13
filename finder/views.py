from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from .models import Post

class FinderPageView(ListView):
    model = Post
    template_name = 'finder.html'
    context_object_name = 'all_posts_list'

class FinderDetailView(DetailView):
    model = Post
    template_name = 'finder_detail.html'

class FinderNewView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'finder_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

class FinderEditView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'finder_edit.html'
    fields = ['title', 'body']

    def dispatch(self, request, *args, **kwargs):  # new
        obj = self.get_object()

        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class FinderDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'finder_delete.html'
    success_url = reverse_lazy('finder:home')

    def dispatch(self, request, *args, **kwargs):  # new
        obj = self.get_object()

        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

