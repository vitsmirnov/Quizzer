from django.db import models


# from django.contrib.auth import get_user_model
# from django.conf import settings
# settings.AUTH_USER_MODEL


class Quiz(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)

    def __str__(self) -> str:
        return f'Quiz: "{self.title}"'
    
    @property
    def points(self) -> int:
        res = 0
        for question in self.questions.all():
            res += question.points
        return res


class Question(models.Model):
    text = models.CharField(max_length=512)
    quiz = models.ForeignKey(to=Quiz, on_delete=models.CASCADE,
                             related_name='questions')
    points = models.IntegerField(default=0)  # Amount of points for correct answer
    
    # Each question has to have the correct answer, but the
    # implementation below doesn't work, so there is a
    # table (class CorrectAnswer) below
    # correct_answer = models.ForeignKey(to='Answer', on_delete=models.CASCADE,
    #                                  related_name='correct_for_questions')
    # An alternative way is to store an id of the correct answer,
    # but I don't think that this is a good idea
    # correct_answer_id = models.IntegerField()

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
    """ Correct answers for each question """
    question = models.OneToOneField(to=Question, on_delete=models.CASCADE,
                                    related_name='correct_answer')
    answer = models.ForeignKey(to=Answer, on_delete=models.CASCADE)
    
    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('question', 'answer'),
                name='unique_correct_answers'
            ),
        )
    
    def __str__(self) -> str:
        return f'Correct answer: "{self.answer}"'
