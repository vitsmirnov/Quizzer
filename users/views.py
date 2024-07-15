from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from .forms import CreationForm

# Create your views here.

class RegisterView(CreateView):
    form_class = CreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login') # 'login'


class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template = 'users/profile.html'

    