from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, max_length=150, verbose_name='Email')
    first_name = models.CharField(max_length=100, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', **NULLABLE)
    preview = models.ImageField(upload_to='user/', verbose_name='Превью', **NULLABLE)
    telegram_id = models.CharField(max_length=20, verbose_name='Телеграм', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Активность')
    code = models.CharField(max_length=10, verbose_name='Код подтверждения', **NULLABLE)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

