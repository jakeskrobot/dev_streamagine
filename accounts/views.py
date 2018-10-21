from .forms import CustomUserCreationForm
from django.views import generic
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from .models import CustomUser


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class AccountsEditView(UpdateView):
    model = CustomUser
    template_name = 'account_edit.html'
    fields = ['username', 'first_name', 'last_name', 'email', 'age', 'twitch_username']
