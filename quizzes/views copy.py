from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .models import Quiz, Question, Answer


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
        # print('CONTEXT:', context)
        # print('KWARGS:', kwargs)
        # print('USER:', self.request.user)

        user = self.request.user
        is_passed = user.is_quiz_passed(self.object.id)
        context['is_passed'] = is_passed
        if is_passed:
            context['answers'] = user.quiz_answers(self.object.id)
            context['score'] = user.score_for_quiz(self.object.id)
        # print('CONTEXT2:', context)
        return context
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        print('QuizView.get()')
        return super().get(request, *args, **kwargs)

    # def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    #     # return super().get(request, *args, **kwargs)
    #     # response = super().get(request, *args, **kwargs)
    #     print('QuizView.get()')

    #     user = request.user
    #     quiz_id = self.get_object().id #int(kwargs['pk'])
    #     # print(user)
    #     # print(user.answers.all())
    #     # print(f'pk = {kwargs['pk']}')
    #     # user.is_quiz_passed(self.model.objects.get(pk=int(kwargs['pk'])))
    #     if user.is_quiz_passed(quiz_id):
    #         return render(request, 'quizzes/result.html', {
    #             'answers': user.quiz_answers(quiz_id),
    #             # 'quiz': self.get_object(), #Quiz.objects.filter(pk=quiz_id).first(),
    #         })

    #     return super().get(request, *args, **kwargs) #response
    
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        user = request.user
        print('QuizView.post()')
        # print('REQUEST.POST:', request.POST)
        # print('KWARGS', kwargs)
        # print('ARGS:', args)
        answers = request.POST.copy()  # Do we need to copy? Probably no.
        answers.pop('csrfmiddlewaretoken')  # It's doubtful
        for answer_id in answers.values():
            answer = Answer.objects.get(pk=int(answer_id))
            user.answers.add(answer)
            if answer.is_correct:
                user.balance += answer.question.points

        user.save()
        
        # quiz_id = kwargs['pk']  # self.get_object().id  # pk

        # Is it the same as redirect() ??
        # return self.get(request, *args, **kwargs)  # redirect?
        # return HttpResponseRedirect(reverse('quizzes:quiz', args=(kwargs['pk'],)))
        return redirect('quizzes:quiz', **kwargs)
