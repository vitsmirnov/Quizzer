from typing import Any
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Quiz, Answer


class QuizListView(ListView):
    model = Quiz
    template_name = 'quizzes/quiz_list.html'
    # paginate_by = # to do!


class QuizView(LoginRequiredMixin, DetailView):
    login_url = 'users:login'
    model = Quiz
    template_name = 'quizzes/quiz.html'
    # context_object_name = 'quiz'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        is_passed = user.is_quiz_passed(self.object.id)
        context['is_passed'] = is_passed
        if is_passed:
            context['answers'] = user.quiz_answers(self.object.id)
            context['score'] = user.score_for_quiz(self.object.id)
        return context

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        user = request.user
        # print('REQUEST.POST:', request.POST)
        # print('KWARGS', kwargs)
        # print('ARGS:', args)
        answers = request.POST.copy()
        answers.pop('csrfmiddlewaretoken')  # It's doubtful
        for answer_id in answers.values():
            # Validation needed!
            answer = Answer.objects.get(pk=int(answer_id))
            user.answers.add(answer)
            if answer.is_correct:
                user.balance += answer.question.points
        user.save()
        
        return redirect('quizzes:quiz', **kwargs)
        # return self.get(request, *args, **kwargs)  # Is it the same as redirect() ?
