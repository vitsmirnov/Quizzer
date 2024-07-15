from django.db import models


# Models list:
class Quiz(models.Model): ...
class Question(models.Model): ...
class Answer(models.Models): ...

class Quiz(models.Model):
    title = models.CharField()
    description = models.CharField()


class Question(models.Model):
    text = models.CharField()
    test = models.ForeignKey(to=Quiz)
    right_answer = models.ForeignKey(to=Answer, related_name='questions')
    price = models.IntegerField(default=0)


class Answer(models.Model):
    text = models.CharField()
    question = models.ForeignKey(to=Question, related_name='answers')
