# Generated by Django 4.2.7 on 2023-11-14 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0005_alter_newsletter_period_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='client',
            field=models.ManyToManyField(related_name='clients', to='newsletter.client', verbose_name='Клиент для рассылки'),
        ),
    ]
