from django.db import models
from django.contrib.auth.models import AbstractUser

from quizzes.models import Quiz, Answer
from shop.models import Color


class User(AbstractUser):
    balance = models.IntegerField(default=0)
    color = models.ForeignKey(to=Color, on_delete=models.CASCADE,
        related_name='users')  # default= ?
    
    colors = models.ManyToManyField(Color)  # Need to add default (fabrik?)
    # User's answers for quiz questions (statistics)
    answers = models.ManyToManyField(Answer, blank=True)
    # Working with answers like that is probably not optimal
    # and we should create a table for statistics or something like that:
    # passed_quizzees = models.ManyToManyField(Quiz)  # ?!
    # but maybe not..

    @property
    def total_points(self) -> int:  # total_score? rating?
        return (self.answers
            .filter(correctanswer__answer_id=models.F('id'))  # the answer is correct
            .aggregate(sum=models.Sum('question__points'))['sum'] or 0)  # get('question__points__sum', 0)

    def is_quiz_passed(self, quiz_id: int) -> bool:
        return self.answers.filter(question__quiz__id=quiz_id).count() > 0
    
    def score_for_quiz(self, quiz_id: int) -> int:
        return (self.answers  # Check needed
            .filter(question__quiz__id=quiz_id,
                    correctanswer__answer_id=models.F('id'))  # the answer is correct
            .aggregate(models.Sum('question__points'))['question__points__sum'] or 0)
        # correctanswer__answer_id=models.F('id') is the same as: 
        # question__correct_answer__answer__id=models.F('id')

    def passed_quizzes(self) -> set[Quiz]:
        return {answer.question.quiz for answer in self.answers.all()}
    
    def passed_quiz_ids(self) -> set[Quiz]:
        return {answer.question.quiz.id for answer in self.answers.all()}
    
    @property
    def passed_quizzes_count(self) -> int:
        # return self.answers.distinct('question__quiz__id')  # It won't work in SQLite
        # This should be a query to DB!
        return len(self.passed_quizzes())
    
    def quiz_answers(self, quiz_id: int) -> list[Answer]:
        """ It returns the user's answers for particular quiz (id) """
        return [answer for answer in self.answers.filter(question__quiz__id=quiz_id)]
    
    # temp (for debugging)
    def _print_passed_quizzes(self) -> None:
        quizzes = self.passed_quizzes()
        for quiz in quizzes:
            print(quiz)
            for question in quiz.questions.all():
                print(f'\t{ question }')
                for answer in question.answers.all():
                    print(f'\t\t{ answer }')
                print(f'\t\t->\t{ question.right_answer }')
                # user's answer
                # There is no any difference between filter() and get in terms of query execution speed.
                print(f'\t\tu ->\t{ self.answers.filter(question__id=question.id).first() }')
