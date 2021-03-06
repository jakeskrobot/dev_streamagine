from django.urls import path
from django.views.generic.base import TemplateView
from .views import *

app_name = 'finder'
urlpatterns = [
    path('', FinderPageView.as_view(), name='home'),
    path('<int:pk>/', FinderDetailView.as_view(), name='finder_detail'),
    path('new/', FinderNewView.as_view(), name='finder_add'),
    path('<int:pk>/edit/', FinderEditView.as_view(), name='finder_edit'),
    path('<int:pk>/delete/', FinderDeleteView.as_view(), name='finder_delete'),
]