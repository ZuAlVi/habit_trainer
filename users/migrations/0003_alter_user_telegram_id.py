# Generated by Django 4.2.10 on 2024-03-01 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_username_user_preview_user_telegram_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Телеграм'),
        ),
    ]
