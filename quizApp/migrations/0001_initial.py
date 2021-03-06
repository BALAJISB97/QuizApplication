# Generated by Django 3.1.4 on 2020-12-17 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizSet',
            fields=[
                ('quizSetId', models.AutoField(primary_key=True, serialize=False)),
                ('quizName', models.CharField(max_length=20)),
                ('quizAddedTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentName', models.CharField(max_length=30)),
                ('studentRollNumber', models.CharField(max_length=8)),
                ('quizSetAttempted', models.CharField(max_length=30)),
                ('score', models.IntegerField()),
                ('isPassed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('quizQuestionId', models.AutoField(primary_key=True, serialize=False)),
                ('quizQuestion', models.TextField()),
                ('option1', models.CharField(max_length=30)),
                ('option2', models.CharField(max_length=30)),
                ('option3', models.CharField(max_length=30)),
                ('option4', models.CharField(max_length=30)),
                ('answer', models.IntegerField()),
                ('quizSetId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizApp.quizset')),
            ],
        ),
    ]
