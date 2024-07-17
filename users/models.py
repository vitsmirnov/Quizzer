from django.db import models
from django.contrib.auth.models import AbstractUser

from quizzes.models import Quiz, Answer

# from colorfield.fields import ColorField


# from django.conf import settings
# settings.AUTH_USER_MODEL
# get_user_model()

# Create your models here.

# class User: ...
# class Color: ...


class Color(models.Model):
    name = models.CharField(verbose_name='Color name', default='', unique=True,
                            max_length=32)
    # value = models.IntegerField(default=0, unique=True) # str?
    value = models.CharField(default='rgba(255,255,255,1)', max_length=64)  # unique=?
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"Color: {self.name} ({self.value}), price: {self.price}"


class User(AbstractUser):
    balance = models.IntegerField(default=0)
    color = models.ForeignKey(to=Color, on_delete=models.CASCADE,
        related_name='users', null=True, blank=True)  # default= ?
    passed_tests_number = models.IntegerField(default=0)

    colors = models.ManyToManyField(Color)
    answers = models.ManyToManyField(Answer)  # This is probably suboptimal
    # passed_quizzees = models.ManyToManyField(Quiz)  # ?!

    def __str__(self) -> str:
        return super().__str__() + f" balance: {self.balance}"
    
    def is_quiz_passed(self, quiz_id: int, quiz: Quiz=None) -> bool:  # quiz_id: int
        # print(quiz)
        # print(self.answers.all())
        # return self.answers.get()
        for answer in self.answers.all():
            # print(answer.question.quiz == quiz)
            # if answer.question.quiz == quiz:
            if answer.question.quiz.id == quiz_id:
                return True
        return False
    
    def passed_quizzes(self) -> set[Quiz]:
        res = set()
        for answer in self.answers.all():
            res.add(answer.question.quiz)
        return res
    
    # temp
    def print_passed_quizzes(self) -> None:
        quizzes = self.passed_quizzes()
        for quiz in quizzes:
            print(quiz)
            for question in quiz.questions.all():
                print(f'\t{ question }')
                for answer in question.answers.all():
                    print(f'\t\t{ answer }')
                print(f'\t\t->\t{ question.right_answer }')
                # user's answer
                # print(f'\t\tuser\'s->\t{ self.answers.get(question__id=question.id) }')
                # print(f'\t\tuser\'s->\t{ get_or_none(self.answers, question__id=question.id) }')
                # There is no any difference between filter() and get in terms of query execution speed.
                print(f'\t\tu ->\t{ self.answers.filter(question__id=question.id).first() }')
    
    def quiz_answers(self, quiz_id: int) -> list:
        result = list()
        # result = self.answers.get()

        for answer in self.answers.all():
            # print(answer.question.quiz == quiz)
            # if answer.question.quiz == quiz:
            if answer.question.quiz.id == quiz_id:
                result.append(answer)
        
        return result


# temp
def get_or_none(query_set, **kwargs):
    try:
        return query_set.get(**kwargs)
    except:  # ?.DoesNotExist:
        return None