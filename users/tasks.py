from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from users.models import User


@shared_task
def verifications(user_id):
    user = User.objects.get(pk=user_id)
    send_mail(
        subject='Подтверждение регистрации',
        message=f'Для подтверждения перейдите по ссылке: "http://localhost:8000/user/activate/" \nВаш новый код: {user.code}, \nВаш id: {user.id}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email]
    )