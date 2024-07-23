from collections.abc import Sequence
from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.db.models import OuterRef, Sum, Subquery, Count, Case, IntegerField, Value, When, Exists, F#, RawSQL  # Going to use it
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.http import HttpRequest, HttpResponse

from .forms import CreationForm
from quizzes.models import Question, Answer, CorrectAnswer
from .models import User
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
        # temporary solution. There should be an ORM query
        return super().get_queryset().raw('\
            SELECT * FROM "users_user"\
            ORDER BY (\
                SELECT SUM("quizzes_question"."points")\
                FROM "quizzes_answer"\
                INNER JOIN "users_user_answers"\
                ON ("quizzes_answer"."id" = "users_user_answers"."answer_id")\
                INNER JOIN "quizzes_correctanswer"\
                ON ("quizzes_answer"."id" = "quizzes_correctanswer"."answer_id")\
                INNER JOIN "quizzes_question"\
                ON "quizzes_answer"."question_id" = "quizzes_question"."id"\
                WHERE ("users_user_answers"."user_id" = "users_user"."id" AND\
                    "quizzes_correctanswer"."answer_id" = ("quizzes_answer"."id"))\
            ) DESC;\
        ')


@login_required(login_url='users:login')
def profile_redirect(request: HttpRequest) -> HttpResponse:
    return redirect('users:profile', pk=request.user.id)
