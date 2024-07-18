from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse
from django.http import HttpRequest, HttpResponse

from .forms import CreationForm
from .models import Color


# USER = get_user_model()


class RegisterView(CreateView):
    form_class = CreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class UserListView(ListView):
    model = get_user_model()  # USER
    template_name = 'users/user_list.html'
    # paginate_by =  # to do!
    # ordering = ['balance', 'username']


class ProfileView(LoginRequiredMixin, DetailView):
    login_url = 'users:login'
    model = get_user_model()
    template_name = 'users/profile.html'


# This should be FormView?
class ColorListView(LoginRequiredMixin, ListView):
    login_url = 'users:login'
    model = Color
    template_name = 'users/colors.html'
    # paginate_by = # to do!

    # buy color should be here
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)



# temp!
def auth_user_profile(request: HttpRequest) -> HttpResponse:
    return redirect('users:profile', pk=request.user.id)


# This is not good!
# This should be in ProfileView (probably)
def change_color(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        request.user.color = request.user.colors.get(pk=request.POST['choice'])
        request.user.save()
    return redirect('users:profile2')


# This should be in ColorListView (post)
def buy_color(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST' and request.user.is_authenticated:
        print(request.POST)
        color_id = int(request.POST['color_id'])
        color = Color.objects.filter(pk=color_id).first()
        user = request.user
        if user.balance >= color.price:
            user.balance -= color.price
            user.colors.add(color)
            user.save()            
            return redirect('users:profile', pk=request.user.id)
        else:
            return redirect('users:colors')
    # return redirect('users:profile', pk=request.user.id)
    return redirect('users:colors')
