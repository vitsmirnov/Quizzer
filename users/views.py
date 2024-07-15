from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CreationForm

# Create your views here.

class RegisterView(CreateView):
    form_class = CreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login') # 'login'
    