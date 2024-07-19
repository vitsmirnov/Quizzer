from django import template

from users.models import User

register = template.Library()

@register.simple_tag
def is_quiz_passed_by_user(quiz_id: int, user: User) -> bool:
    return user.is_quiz_passed(quiz_id)

@register.simple_tag
def user_score_for_quiz(user: User, quiz_id: int) -> int:
    return user.score_for_quiz(quiz_id)
