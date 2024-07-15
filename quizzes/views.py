from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Quiz

# Create your views here.

def index(request):
    return render(request, 'quizzes/index.html')


class QuizzesView(ListView):
    model = Quiz
    template_name = 'quizzes/quizzes.html'

