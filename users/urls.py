from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import (
    RegisterView, ProfileView, UserListView, profile_redirect
)


app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html',
        next_page='quizzes:quiz_list'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html',
        next_page='quizzes:quiz_list'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('change_password/', ),

    # Profile doesn't need a pk, because it's login required (shows only for themselves). Or not?
    # Or it could use a username insted of pk
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/', profile_redirect, name='profile_redirect'),
    path('', UserListView.as_view(), name='user_list'),
]
