from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .forms import CreationForm
from .views import RegisterView, ProfileView, profile2, ColorListView, \
    change_color, UserListView

app_name = 'users'

urlpatterns = [
    # path('auth/login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('login/', LoginView.as_view(template_name='users/login.html',
        next_page='users:profile2'), name='login'), #redirect_field_name # go to profile!
    path('logout/', LogoutView.as_view(template_name='users/logout.html',
        next_page='quizzes:quiz_list'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('change_password/'),

    path('', UserListView.as_view(), name='user_list'),  # 'users/' or 'list/' ??

    path('profile/', profile2, name='profile2'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    # path('profile/<str:username>', ProfileView.as_view(), name='profile'),

    path('colors/', ColorListView.as_view(), name='colors'),
    path('change_color/', change_color, name='change_color'),
]
