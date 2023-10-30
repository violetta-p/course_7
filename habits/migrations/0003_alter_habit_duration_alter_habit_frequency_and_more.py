# Generated by Django 4.2.6 on 2023-10-30 19:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_alter_habit_duration_alter_habit_frequency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(seconds=120), verbose_name='Duration of action'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='frequency',
            field=models.DurationField(default=datetime.timedelta(seconds=28800), verbose_name='Interval'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.TimeField(default='12:00', verbose_name='Action execution time'),
        ),
        migrations.AlterField(
            model_name='relatedhabit',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(seconds=120), verbose_name='Duration of action'),
        ),
    ]
