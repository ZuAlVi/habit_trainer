import re
from rest_framework.serializers import ValidationError


class TimeValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_time = dict(value).get(self.field)
        if tmp_time > 120:
            raise ValidationError('Время не должно быть больше 120 секунд')


class HabitPleasantValidator:

    def __init__(self, is_pleasant, related_habit, fee):
        self.is_pleasant = is_pleasant
        self.related_habit = related_habit
        self.fee = fee

    def __call__(self, value):
        tmp_is_pleasant = dict(value).get(self.is_pleasant)
        tmp_related_habit = dict(value).get(self.related_habit)
        tmp_fee = dict(value).get(self.fee)
        if tmp_is_pleasant and (tmp_related_habit or tmp_fee):
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")


class HabitFeeValidator:
    def __init__(self, related_habit, fee):
        self.related_habit = related_habit
        self.fee = fee

    def __call__(self, value):
        tmp_habit = dict(value).get(self.related_habit)
        tmp_fee = dict(value).get(self.fee)
        if tmp_habit and tmp_fee:
            raise ValidationError("Нельзя одновременно выбрать связанную привычку и указать вознаграждение.")

