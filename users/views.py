from collections.abc import Sequence
from typing import Any
from django.db.models.query import QuerySet
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

    def get_ordering(self) -> Sequence[str]:
        ordering = super().get_ordering()
        print('UserListView.get_ordering():', ordering, '\n')
        return ordering
    
    def get_queryset(self) -> QuerySet[Any]:
        # return super().get_queryset() #.order_by()

        queryset = super().get_queryset()
        print('UserListView.get_queryset():', queryset, '\n')
        # It's ok if list of users isn't very big
        # print(type(queryset))
        queryset = sorted(queryset, key=lambda user: user.total_points, #passed_quizzes_count,
                          reverse=True)
        # queryset = QuerySet(queryset)
        # print(type(queryset))
        return queryset

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        # ordering here
        # print('UserListView.get_context_data:', context)
        # # print('object_list:', context['object_list'])#self.object_list)
        # ol = context['object_list']
        # ol = ol.order_by('balance')
        # context['object_list'] = ol
        # # print('object_list2:', context['object_list'])#self.object_list)
        # print('UserListView.get_context_data:', context)
        # print()
        context['sorted_by_points'] = sorted(
            self.get_queryset(),
            key=lambda user: user.total_points, #passed_quizzes_count,
            reverse=True
        )
        return context


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
