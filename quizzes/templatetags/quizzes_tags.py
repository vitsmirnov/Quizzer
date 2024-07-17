from django import template

from users.models import User

register = template.Library()

@register.simple_tag
def is_quiz_passed_by_user(quiz_id: int, user: User) -> bool:
    return user.is_quiz_passed(quiz_id)
