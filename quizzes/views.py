from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Quiz, Question, Answer

# Create your views here.

def index(request):
    return render(request, 'quizzes/index.html')


class QuizListView(ListView):
    model = Quiz
    template_name = 'quizzes/quiz_list.html'


class QuizView(DetailView):#ListView):
    model = Quiz  #Question
    template_name = 'quizzes/quiz.html'
    # context_object_name = 'questions'

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
