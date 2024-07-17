from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


class Quiz(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)

    def __str__(self) -> str:
        return f'Quiz: "{self.title}"'


class Question(models.Model):
    text = models.CharField(max_length=512)
    quiz = models.ForeignKey(to=Quiz, on_delete=models.CASCADE,
                             related_name='questions')
    
    # correct_answer = models.ForeignKey(to='Answer', on_delete=models.CASCADE,
    #                                  related_name='questions2')
    # correct_answer = models.OneToOneField(to='Answer', on_delete=models.CASCADE,
    #                                     related_name='right_for_question')
    # correct_answer = models.IntegerField()

    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'Question: "{self.text}" (quiz: {self.quiz.title})'


class Answer(models.Model):
    text = models.CharField(max_length=512)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE,
                                 related_name='answers')
    
    def __str__(self) -> str:
        return f'Answer: "{self.text}" (question: {self.question})'
    
    @property
    def is_correct(self) -> bool:
        return self.id == self.question.correct_answer.answer.id
    

class CorrectAnswer(models.Model):
    """ Right answers for each question """
    question = models.OneToOneField(to=Question, on_delete=models.CASCADE,
                                    related_name='correct_answer')
    answer = models.ForeignKey(to=Answer, on_delete=models.CASCADE)#,
                               #related_name='questions')  # remove related_name?
    
    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('question', 'answer'),
                name='correct_answers'  # ?
            ),
        )
    
    def __str__(self) -> str:
        return f'Correct answer: "{self.answer}"'
