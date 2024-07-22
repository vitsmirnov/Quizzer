from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Quiz, Answer


class QuizListView(ListView):
    model = Quiz
    template_name = 'quizzes/quiz_list.html'
    paginate_by = 1  # This shouldn't be hardcoded I guess


class QuizView(LoginRequiredMixin, DetailView):
    login_url = 'users:login'
    model = Quiz
    template_name = 'quizzes/quiz.html'
    # context_object_name = 'quiz'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        is_passed = user.is_quiz_passed(self.get_object().id)#self.object.id
        context['is_passed'] = is_passed
        if is_passed:
            context['answers'] = user.quiz_answers(self.get_object().id)#self.object.id)
            context['score'] = user.score_for_quiz(self.get_object().id)#self.object.id)
        return context

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        answers = request.POST.copy()
        answers.pop('csrfmiddlewaretoken')  # It's doubtful
        if len(answers) == 0:  # There are no answers
            # Why will this not work?
            # context = self.get_context_data(**kwargs)
            # context['message'] = 'You haven\'t chosen any answer'
            # return self.render_to_response(request, self.template_name, context)
            
            # I'm not shure about that
            return self.render_to_response({
                'message': 'You haven\'t chosen any answer',
                'object': self.get_object(),  # This is doubtful
            })
        user = request.user
        for answer_id in answers.values():
            # Validation needed!
            answer = Answer.objects.get(pk=int(answer_id))
            user.answers.add(answer)
            if answer.is_correct:
                user.balance += answer.question.points
        user.save()
        
        return redirect('quizzes:quiz', **kwargs)
        # return self.get(request, *args, **kwargs)  # Is it the same as redirect() ?


class UserQuizzesView(LoginRequiredMixin, ListView):
    login_url = 'users:login'
    model = Quiz
    template_name = 'quizzes/quiz_list.html'

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(
            pk__in=self.request.user.passed_quiz_ids())
