from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from .forms import CreationForm
from .models import Color


user = get_user_model()

# Create your views here.

class RegisterView(CreateView):
    form_class = CreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login') # 'login'


class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'users/profile.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context[''] = timezone.now()
    #     return context

def profile2(request):
    return redirect('users:profile', pk=request.user.id)


class ColorListView(ListView):
    model = Color
    template_name = 'users/colors.html'


def change_color(request):
    # print('CHANGE_COLOR')
    if request.method == 'POST':
        # print(request.POST['choice'])
        # request
        # print(request.user)
        # print(request.user.colors.get(pk=request.POST['choice']))
        request.user.color = request.user.colors.get(pk=request.POST['choice'])
        request.user.save()
        # print(request.user, '\n', user)

    return redirect('users:profile2')


class UserListView(ListView):
    model = user
    template_name = 'users/user_list.html'

    # def get_context_data(self, **kwargs: reverse_lazy) -> dict[str, Any]:
    #     # return super().get_context_data(**kwargs)
    #     context = super().get_context_data(**kwargs)
    #     # self.object_list.
    #     return context
