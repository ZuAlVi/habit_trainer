from django.conf import settings
from django.db import models

from users.models import NULLABLE


class RelatedHabit(models.Model):
    activity = models.CharField(max_length=150, verbose_name='Активность')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.SET_NULL,
                             **NULLABLE)

    def __str__(self):
        return self.activity

    class Meta:
        verbose_name = 'Сопутствующая ривычка'
        verbose_name_plural = 'Сопутствующие привычки'


class Habit(models.Model):
    period = [
        ('week', 'Раз в неделю'),
        ('every_day', 'Каждый день')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    place = models.CharField(max_length=150, verbose_name='Место выполнения')
    usual_time = models.DateTimeField(verbose_name='Время выполнения')
    activity = models.CharField(max_length=100, verbose_name='Активность')
    is_pleasant = models.BooleanField(default=False, verbose_name='Признак приятности')
    related_habit = models.ForeignKey(RelatedHabit, verbose_name='Связанная привычка', on_delete=models.CASCADE,
                                      **NULLABLE)
    periodicity = models.CharField(max_length=9, default='every_day', choices=period, verbose_name='Переодичност')
    fee = models.CharField(max_length=150, verbose_name='Вознагрождение', **NULLABLE)
    time_to_complete = models.PositiveIntegerField(default=1, verbose_name='Время выполнения')
    is_published = models.BooleanField(default=False, verbose_name='Публикация')

    def __str__(self):
        return self.activity

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
