from django.utils import timezone
from datetime import datetime, timedelta
import pytz
import requests
from habit.models import Habit
from celery import shared_task
from django.conf import settings


@shared_task
def message():
    timezone.activate('Europe/Moscow')
    today = datetime.now()
    moskow_tz = pytz.timezone('Europe/Moscow')
    today = today.astimezone(moskow_tz)
    habit_list = Habit.objects.all()
    for habit in habit_list:
        if habit.periodicity == 'daily' and habit.usual_time <= today:
            params = {'chat_id': f'{habit.user.telegram_id}',
                      "text": f"Эй ты{habit.user.last_name}, пришло время для {habit.activity},"
                      }
            requests.get(f'https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage', params=params).json()
            habit.usual_time = datetime.now().astimezone(moskow_tz) + timedelta(days=1)
            habit.save()
        elif habit.periodicity == 'weekly' and habit.usual_time <= today:
            params = {'chat_id': f'{habit.user.telegram_id}',
                      "text": f"Эй ты{habit.user.last_name}, пришло время для {habit.activity}"
                      }
            requests.get(f'https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage', params=params).json()
            habit.usual_time = datetime.now().astimezone(moskow_tz) + timedelta(days=7)
            habit.save()
