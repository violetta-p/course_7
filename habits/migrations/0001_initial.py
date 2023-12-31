# Generated by Django 4.2.6 on 2023-11-02 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=100, null=True, verbose_name='Location')),
                ('time', models.TimeField(default='12:00', verbose_name='Action execution time')),
                ('action', models.CharField(max_length=200, verbose_name='Action')),
                ('is_pleasant', models.BooleanField(default=False, verbose_name='Is pleasant')),
                ('frequency', models.DurationField(default=datetime.timedelta(seconds=28800), verbose_name='Interval')),
                ('reward', models.CharField(blank=True, max_length=200, null=True, verbose_name='Reward')),
                ('duration', models.DurationField(default=datetime.timedelta(seconds=120), verbose_name='Duration of action')),
                ('is_public', models.BooleanField(default=False, verbose_name='A sign of a public habit')),
                ('last_execution_time', models.DateTimeField(auto_now=True, verbose_name='Last execution')),
            ],
            options={
                'verbose_name': 'Habit',
                'verbose_name_plural': 'Habits',
            },
        ),
        migrations.CreateModel(
            name='RelatedHabit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=100, null=True, verbose_name='Location')),
                ('action', models.CharField(max_length=200, verbose_name='Action')),
                ('duration', models.DurationField(default=datetime.timedelta(seconds=120), verbose_name='Duration of action')),
                ('is_public', models.BooleanField(default=True, verbose_name='is public')),
            ],
            options={
                'verbose_name': 'Related habit',
                'verbose_name_plural': 'Related habits',
            },
        ),
    ]
