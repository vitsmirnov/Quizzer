from django.urls import path

from .views import QuizListView, QuizView, UserQuizzesView


app_name = 'quizzes'

urlpatterns = [
    path('', QuizListView.as_view(), name='quiz_list'),
    path('<int:pk>/', QuizView.as_view(), name='quiz'),
    path('result/', UserQuizzesView.as_view(), name='user_result')
]
