from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    # path('auth/login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('', LoginView.as_view(template_name='users/login.html',
        next_page='quizzes:index'), name='login'), #redirect_field_name
    path('logout/', LogoutView.as_view(template_name='users/logout.html',
        next_page='quizzes:index'), name='logout'),
]
