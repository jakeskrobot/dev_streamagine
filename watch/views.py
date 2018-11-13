from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import *

class WatchHomeView(ListView):
    model = CustomUser
    template_name = 'watch.html'
    context_object_name = 'all_twitch_username'

class WatchStreamView(DetailView):
    model = CustomUser
    template_name = 'watch_stream.html'
    context_object_name = 'all_twitch_username'

class WatchAddView(CreateView):
    model = Stream
    template_name = 'watch_add.html'
    fields = ['stream_name', 'author']