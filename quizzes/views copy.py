from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Quiz, Question, Answer


class QuizListView(ListView):
    model = Quiz
    template_name = 'quizzes/quiz_list.html'


class QuizView(LoginRequiredMixin, DetailView):
    login_url = 'users:login'
    model = Quiz
    template_name = 'quizzes/quiz.html'
    # context_object_name = 'quiz'

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     #
    #     return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # return super().get(request, *args, **kwargs)
        rensponse = super().get(request, *args, **kwargs)
        print('QuizView.get()')

        user = request.user
        quiz_id = int(kwargs['pk'])
        # print(user)
        # print(user.answers.all())
        # print(f'pk = {kwargs['pk']}')
        # user.is_quiz_passed(self.model.objects.get(pk=int(kwargs['pk'])))
        if user.is_quiz_passed(quiz_id):
            return render(request, 'quizzes/result.html', {
                'answers': user.quiz_answers(quiz_id),
                'quiz': Quiz.objects.filter(pk=quiz_id).first(),
            })

        return rensponse
    
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # return super().get(request, *args, **kwargs)
        # rensponse = super().post(request, *args, **kwargs)

        user = request.user
        print('QuizView.post()')
        # print(f'submit_quiz({quiz_id}, {user_id})')
        # print(request.POST)
        # return render(request, 'quizzes/passed_quiz.html', {
        #     'quiz_id': quiz_id, 'user_id': user_id,
        # })
        # print(request.POST)
        answers = request.POST.copy()
        answers.pop('csrfmiddlewaretoken')  # It's doubtful
        # for k, v in answers.items():
        for v in answers.values():
            answer = Answer.objects.get(pk=int(v))
            user.answers.add(answer)
            if answer.is_correct:
                user.balance += answer.question.points

        user.save()
        
        quiz_id = int(kwargs['pk'])
    
        return render(request, 'quizzes/result.html', {
            'answers': user.quiz_answers(quiz_id),
            'quiz': Quiz.objects.filter(pk=quiz_id).first(),
        }) #context

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        # return super().get_context_data(**kwargs)
        # quizzes = super().get_context_data(**kwargs)
        # for v in kwargs:
        #     print(v)
        # q = kwargs['object']
        # print(kwargs['object'])
        # print(quizzes)
        # print(type(q).__dict__)# .objects.all())

        # print(self.object.questions.all())
        # for o in self.object.questions.all():
        #     print(o)

        # return self.object.questions.all() #quizzes
        
        # context = super().get_context_data(**kwargs)
        # context['questions'] = self.object.questions.all()
        # context['answers'] = None

        # return context


# class Submit

def submit_quiz(request, quiz_id, user_id):
    if request.method == 'POST':
        print(f'submit_quiz({quiz_id}, {user_id})')

        # print(request.POST)

        return render(request, 'quizzes/passed_quiz.html', {
            'quiz_id': quiz_id, 'user_id': user_id,
        })
    return redirect('users:login')
