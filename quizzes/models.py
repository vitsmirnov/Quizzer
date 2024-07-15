from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
# from settings import AUTH_USER_MODEL

# Models list:
# class Quiz(models.Model): ...
# class Question(models.Model): ...
# class Answer(models.Model): ...


class Quiz(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)

    def __str__(self) -> str:
        return f'Quiz: "{self.title}"'


class Question(models.Model):
    text = models.CharField(max_length=512)
    # rename to quiz??!
    test = models.ForeignKey(to=Quiz, on_delete=models.CASCADE,
                             related_name='questions')
    # right_answer = models.ForeignKey(to=Answer, on_delete=models.CASCADE,
    #                                  related_name='question2')
    # right_answer = models.OneToOneField(to='Answer', on_delete=models.CASCADE,
    #                                     related_name='right_for_question')
    # right_answer = models.ForeignKey(to='quizzes.Answer', on_delete=models.CASCADE,
    #                                  related_name='questions')
    # right_answer = models.IntegerField()
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'Question: "{self.text}" (test: {self.test})'


class Answer(models.Model):
    text = models.CharField(max_length=512)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE,
                                 related_name='answers')
    
    def __str__(self) -> str:
        return f'Answer: "{self.text}" (to question: {self.question})'
    

class QuestionAnswer(models.Model):
    """ Right answers for each question """
    question = models.OneToOneField(to=Question, on_delete=models.CASCADE,
                                    related_name='right_answer')
    answer = models.ForeignKey(to=Answer, on_delete=models.CASCADE,
                               related_name='questions')
    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('question', 'answer'),
                name='right_answers'
            ),
        )
    
    def __str__(self) -> str:
        return f'For question "{self.question}" right answer is "{self.answer}"'


class UserAnswer(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='answers') # OneToOneField()
    answer = models.ForeignKey(to=Answer, on_delete=models.CASCADE,
                               related_name='users') # delete related_name
    
    # quiz = models.ForeignKey(to=Quiz, on_delete=models.CASCADE)

    # class Meta:
    #     constraints = (
    #         models.UniqueConstraint(
    #             fields=('question', 'answer'),
    #             name='right_answers'
    #         ),
    #     )
    
    # def __str__(self) -> str:
    #     return f'For question "{self.question}" right answer is "{self.answer}"'
