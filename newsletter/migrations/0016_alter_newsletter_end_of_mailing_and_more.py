# Generated by Django 4.2.7 on 2023-11-18 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0015_newsletter_time_mailing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='end_of_mailing',
            field=models.DateTimeField(default='2024-01-01 12:00', verbose_name='Дата и время окончание рассылки'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='time_mailing',
            field=models.TimeField(default=datetime.datetime(2023, 11, 18, 9, 0, 42, 635804, tzinfo=datetime.timezone.utc), verbose_name='Время рассылки'),
        ),
    ]