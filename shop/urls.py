from django.urls import path

from .views import ColorListView


app_name = 'shop'

urlpatterns = [
    path('colors/', ColorListView.as_view(), name='colors'),
]
