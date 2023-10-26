import json
import os
import datetime

from rest_framework import status
from rest_framework.test import APITestCase, APIClient, force_authenticate
from django.urls import reverse

from habits.models import Habit, RelatedHabit
from users.models import User

current_time = datetime.datetime.now()


class HabitTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:

        cls.user = User.objects.create(
            email="Test@mail.ru",
            password="Test12345",
            is_active=True,
        )

        cls.habit = Habit.objects.create(
            location='work',
            time='14:00',
            action='drink water',
            is_pleasant=True,
            frequency='4 hours',
            duration='60 seconds',
            is_public=True
        )
        cls.related_habit = RelatedHabit.objects.create(
            location='work',
            action='drink coffee',
            duration='80 seconds',
            is_public=True
        )

    def test_get_list(self):

        response = self.client.get(
            reverse('habits:habit_list')
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        print(response.json())

    def test_update_habit(self):
        data2 = {
            'location': 'home',
            'time': '14:00',
            'action': 'drink hot water',
            'is_pleasant': True,
            'frequency': '5 hours',
            'duration': '70 seconds',
            'is_public': False
        }
        response = self.client.put(
            reverse('habits:habit_update', kwargs={'pk': self.habit.pk}),
            data=data2,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_habit(self):
        response = self.client.delete(
            reverse('habits:habit_delete', kwargs={'pk': self.habit.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
