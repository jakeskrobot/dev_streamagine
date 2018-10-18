from django.urls import path
from django.views.generic.base import TemplateView

from .views import *

app_name = 'watch'
urlpatterns = [
    path('', TemplateView.as_view(template_name='watch.html'), name='home'),
    path('', WatchHomeView.as_view(), name='home'),
    path('<str:twitch_username>/', WatchStreamView.as_view(), name='watch_stream'),
]