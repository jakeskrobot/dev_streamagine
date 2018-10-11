from django.urls import path
from django.views.generic.base import TemplateView
from .views import *

app_name = 'finder'
urlpatterns = [
    path('', FinderPageView.as_view(), name='home'),
    path('<int:pk>/', FinderDetailView.as_view(), name='finder_detail'),
    path('new/', FinderNewView.as_view(), name='finder_add'),
]