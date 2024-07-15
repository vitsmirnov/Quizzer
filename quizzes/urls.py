from django.urls import path

from .views import index, QuizListView

app_name = 'quizzes'

urlpatterns = [
    # path('', index, name='index'),
    path('', QuizListView.as_view(), name='quiz_list'),#name='index'),
]
