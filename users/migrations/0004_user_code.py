# Generated by Django 4.2.10 on 2024-03-01 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_telegram_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Код подтверждения'),
        ),
    ]
