from django.urls import path

from .views import index, QuizListView, QuizView, submit_quiz

app_name = 'quizzes'

urlpatterns = [
    # path('', index, name='index'),
    path('', QuizListView.as_view(), name='quiz_list'),#name='index'),
    path('quiz/<int:pk>/', QuizView.as_view(), name='quiz'),
    path('quiz/<int:quiz_id>/<int:user_id>/', submit_quiz, name='submit_quiz'),
]
