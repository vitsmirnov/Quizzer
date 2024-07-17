from django.urls import path

from .views import index, QuizListView, QuizView, submit_quiz


app_name = 'quizzes'

urlpatterns = [
    # path('', index, name='index'),
    path('', QuizListView.as_view(), name='quiz_list'),#name='index'),
    path('quiz/<int:pk>/', QuizView.as_view(), name='quiz'),
    
    # path('submit_quiz/<int:quiz_id>/<int:user_id>/', submit_quiz, name='submit_quiz'),
    # path('quiz/<int:pk>/submit/', submit_quiz, name='submit'),
    # path('quiz/<int:pk>/result/', submit_quiz, name='result'),
]
