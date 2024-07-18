from django.urls import path

from .views import QuizListView, QuizView


app_name = 'quizzes'

urlpatterns = [
    path('', QuizListView.as_view(), name='quiz_list'),#name='index'),
    path('quiz/<int:pk>/', QuizView.as_view(), name='quiz'),
    
    # path('quiz/<int:pk>/submit/', submit_quiz, name='submit'),
    # path('quiz/<int:pk>/result/', submit_quiz, name='result'),
]
