from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .models import User, Color

# Register your models here.

# admin.site.register(User, UserAdmin)
admin.site.register(get_user_model())#, UserAdmin)
admin.site.register(Color)


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username', 'email', 'is_active', 'last_login', 'is_staff', )
#     readonly_fields = (
#         'password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name',
#         'email', 'balance', 'color', 'passed_tests', 'date_joined', 'username',
#     )
#     empty_value_display = VALUE_DISPLAY

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username', 'email', 'is_active', 'last_login', 'is_staff', )
#     readonly_fields = (
#         'password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name',
#         'email', 'balance', 'color', 'passed_tests', 'date_joined', 'username',
#     )
#     empty_value_display = VALUE_DISPLAY
