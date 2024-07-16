from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Quiz, Question, Answer

# Create your views here.

def index(request):
    return render(request, 'quizzes/index.html')


class QuizListView(ListView):
    model = Quiz
    template_name = 'quizzes/quiz_list.html'


class QuizView(LoginRequiredMixin, DetailView):#ListView):
    model = Quiz  #Question
    template_name = 'quizzes/quiz.html'
    # context_object_name = 'questions'

    login_url = 'users:login'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # return super().get(request, *args, **kwargs)
        rensponse = super().get(request, *args, **kwargs)
        print('QuizView.get()')

        user = request.user
        print(user)
        print(f'pk = {kwargs['pk']}')
        # user.is_quiz_passed(self.model.objects.get(pk=int(kwargs['pk'])))
        if user.is_quiz_passed(int(kwargs['pk'])):
            return render(request, 'quizzes/result.html', {
                'quiz_id': 404,
                'user_id': 404,
            })

        return rensponse
    
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # return super().get(request, *args, **kwargs)
        # rensponse = super().post(request, *args, **kwargs)

        print('QuizView.post()')
        # print(f'submit_quiz({quiz_id}, {user_id})')
        # print(request.POST)
        # return render(request, 'quizzes/passed_quiz.html', {
        #     'quiz_id': quiz_id, 'user_id': user_id,
        # })
        print(request.POST)
    
        return render(request, 'quizzes/result.html', {
            'quiz_id': 404,
            'user_id': 404,
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


def submit_quiz(request, quiz_id, user_id):
    if request.method == 'POST':
        print(f'submit_quiz({quiz_id}, {user_id})')

        print(request.POST)

        return render(request, 'quizzes/passed_quiz.html', {
            'quiz_id': quiz_id, 'user_id': user_id,
        })
    return redirect('users:login')

# class Submit
