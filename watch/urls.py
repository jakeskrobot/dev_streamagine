from django.urls import path
from django.views.generic.base import TemplateView

app_name = 'watch'
urlpatterns = [
    path('', TemplateView.as_view(template_name='watch.html'), name='home'),
]