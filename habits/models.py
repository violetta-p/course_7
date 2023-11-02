from datetime import timedelta

from django.db import models
from config import settings

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """
    Модель привычки.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             verbose_name='User',
                             **NULLABLE)
    location = models.CharField(max_length=100,
                                verbose_name='Location',
                                **NULLABLE)
    time = models.TimeField(default='12:00',
                            verbose_name='Action execution time')
    action = models.CharField(max_length=200,
                              verbose_name='Action')
    is_pleasant = models.BooleanField(default=False,
                                      verbose_name='Is pleasant')
    related_habit = models.ForeignKey('RelatedHabit',
                                      on_delete=models.SET_NULL,
                                      verbose_name='Related action',
                                      **NULLABLE)
    frequency = models.DurationField(default=timedelta(hours=8),
                                     verbose_name='Interval')
    reward = models.CharField(max_length=200,
                              verbose_name='Reward',
                              **NULLABLE)
    duration = models.DurationField(default=timedelta(seconds=120),
                                    verbose_name='Duration of action')
    is_public = models.BooleanField(default=False,
                                    verbose_name='A sign of a public habit')
    last_execution_time = models.DateTimeField(auto_now=True,
                                               verbose_name='Last execution')

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Habit'
        verbose_name_plural = 'Habits'


class RelatedHabit(models.Model):
    """
    Экземпляры данного класса (по определению являются
    приятными привычками) - это объекты, которые могут
    быть выбраны в дальнейшем в качестве связанной привычки.

    Приятные привычки могут быть созданы всеми пользователями.
    В дальнейшем, при создании привычки (модель Habit), пользователь
    может добавить как приятную привычку из созданных им ранее, так и
    приятную привычку, созданную другими пользователями (при условии
    наличия отметки is_public).

    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             verbose_name='User',
                             **NULLABLE)
    location = models.CharField(max_length=100,
                                verbose_name='Location',
                                **NULLABLE)
    action = models.CharField(max_length=200,
                              verbose_name='Action')
    duration = models.DurationField(default=timedelta(seconds=120),
                                    verbose_name='Duration of action')
    is_public = models.BooleanField(default=True,
                                    verbose_name='is public')

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Related habit'
        verbose_name_plural = 'Related habits'
