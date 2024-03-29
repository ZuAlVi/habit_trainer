# Generated by Django 4.2.10 on 2024-03-02 05:20

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
            name='RelatedHabit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=150, verbose_name='Активность')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Сопутствующая ривычка',
                'verbose_name_plural': 'Сопутствующие привычки',
            },
        ),
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=150, verbose_name='Место выполнения')),
                ('usual_time', models.DateTimeField(verbose_name='Время выполнения')),
                ('activity', models.CharField(max_length=100, verbose_name='Активность')),
                ('is_pleasant', models.BooleanField(default=False, verbose_name='Признак приятности')),
                ('periodicity', models.CharField(choices=[('week', 'Раз в неделю'), ('every_day', 'Каждый день')], default='every_day', max_length=9, verbose_name='Переодичност')),
                ('fee', models.CharField(blank=True, max_length=150, null=True, verbose_name='Вознагрождение')),
                ('time_to_complete', models.PositiveIntegerField(default=1, verbose_name='Время выполнения')),
                ('is_published', models.BooleanField(default=False, verbose_name='Публикация')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habit.relatedhabit', verbose_name='Связанная привычка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]
