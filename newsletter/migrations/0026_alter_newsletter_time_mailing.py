# Generated by Django 4.2.7 on 2023-11-21 06:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0025_alter_newsletter_time_mailing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='time_mailing',
            field=models.TimeField(default=datetime.datetime(2023, 11, 21, 6, 50, 39, 783674), verbose_name='Время рассылки'),
        ),
    ]
