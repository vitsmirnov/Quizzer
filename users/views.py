from collections.abc import Sequence
from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.db.models import Case, IntegerField, Value, When, Exists, F  # Going to use it
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.http import HttpRequest, HttpResponse

from .forms import CreationForm
# from .models import Color


USER = get_user_model()


class RegisterView(CreateView):
    form_class = CreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class ProfileView(LoginRequiredMixin, DetailView):
    login_url = 'users:login'
    model = USER
    template_name = 'users/profile.html'

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # Validation needed!
        request.user.color = request.user.colors.get(pk=request.POST['choice'])
        request.user.save()
        return redirect('users:profile', pk=request.user.id)


class UserListView(ListView):
    model = USER
    template_name = 'users/user_list.html'
    paginate_by = 20  # It probably shouldn't be hardcoded
    # ordering = []  # to do!

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        # Change ordering here
        return queryset

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        # return super().get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        # This is temporary solution. Here should be used query to DB
        # We shuld change ordering in get_queryset method, not here
        context['object_list'] = sorted(
            self.get_queryset(),
            key=lambda user: user.total_points, #passed_quizzes_count,
            reverse=True
        )
        return context


@login_required(login_url='users:login')
def profile_redirect(request: HttpRequest) -> HttpResponse:
    return redirect('users:profile', pk=request.user.id)
