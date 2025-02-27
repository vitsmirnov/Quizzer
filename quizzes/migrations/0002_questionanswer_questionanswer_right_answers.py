# Generated by Django 4.2.14 on 2024-07-15 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quizzes.answer')),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='right_answer', to='quizzes.question')),
            ],
        ),
        migrations.AddConstraint(
            model_name='questionanswer',
            constraint=models.UniqueConstraint(fields=('question', 'answer'), name='right_answers'),
        ),
    ]
