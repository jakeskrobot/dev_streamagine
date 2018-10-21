from django.urls import path
from django.views.generic.base import TemplateView

from . import views
from .views import  *

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('my_account/', TemplateView.as_view(template_name='my_account.html'), name='my_account'),
    path('<int:pk>/edit/', AccountsEditView.as_view(template_name='account_edit.html'), name='edit_account')
]
