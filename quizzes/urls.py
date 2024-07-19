from django.urls import path

from .views import QuizListView, QuizView


app_name = 'quizzes'

urlpatterns = [
    path('', QuizListView.as_view(), name='quiz_list'),
    # path('quiz/<int:pk>/', QuizView.as_view(), name='quiz'),
    path('<int:pk>/', QuizView.as_view(), name='quiz'),
]
