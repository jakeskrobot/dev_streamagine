from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from accounts.models import *

class WatchHomeView(ListView):
    model = CustomUser
    template_name = 'watch.html'
    context_object_name = 'all_twich_username'

class WatchStreamView(DetailView):
    model = CustomUser
    template_name = 'watch_stream.html'
    context_object_name = 'all_twich_username'