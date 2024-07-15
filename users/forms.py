from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)

# class RegisterForm(forms.form):
#     username = forms.CharField(max_langth=32, unique=True, null=False, blank=False)
#     password = forms.CharField(widget=)

class CreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', )
