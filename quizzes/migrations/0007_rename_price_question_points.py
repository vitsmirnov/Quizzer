# Generated by Django 4.2.14 on 2024-07-18 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0006_remove_correctanswer_correct_answers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='price',
            new_name='points',
        ),
    ]
