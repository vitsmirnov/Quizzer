from django.contrib import admin

from .models import Quiz, Question, Answer, RightAnswer

# Register your models here.

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(RightAnswer)
