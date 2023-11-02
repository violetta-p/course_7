import datetime

from rest_framework import status
from rest_framework.test import APITestCase
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
            reward=None,
            is_pleasant=True,
            frequency='5 hours',
            duration='80 seconds',
            is_public=True
        )
        cls.related_habit = RelatedHabit.objects.create(
            location='work',
            action='drink coffee',
            duration='90 seconds',
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

    def test_get_public_habit_list(self):

        response = self.client.get(
            reverse('habits:public_habit_list')
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_habit(self):
        data2 = {
            'location': 'home',
            'time': '14:00',
            'action': 'drink hot water',
            'is_pleasant': True,
            'frequency': datetime.timedelta(seconds=600),
            'duration': datetime.timedelta(seconds=70),
            'is_public': False,
        }

        response = self.client.patch(
            reverse('habits:habit_update', kwargs={'pk': self.habit.pk}),
            data=data2,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_fail_update_habit(self):
        data2 = {
            'location': 'home',
            'time': '14:00',
            'action': 'drink hot water',
            'is_pleasant': True,
            'frequency': datetime.timedelta(seconds=600),
            'duration': datetime.timedelta(seconds=130),
            'is_public': False,
        }

        response = self.client.patch(
            reverse('habits:habit_update', kwargs={'pk': self.habit.pk}),
            data=data2,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_fail_2_update_habit(self):
        data2 = {
            'location': 'home',
            'time': '14:00',
            'action': 'drink hot water',
            'is_pleasant': True,
            'frequency': datetime.timedelta(hours=170),
            'duration': datetime.timedelta(seconds=130),
            'is_public': False,
        }

        response = self.client.patch(
            reverse('habits:habit_update', kwargs={'pk': self.habit.pk}),
            data=data2,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_fail_3_update_habit(self):
        data2 = {
            'location': 'home',
            'time': '14:00',
            'action': 'drink hot water',
            'is_pleasant': True,
            'reward': 'eat',
            'frequency': datetime.timedelta(hours=100),
            'duration': datetime.timedelta(seconds=100),
            'is_public': False,
        }

        response = self.client.patch(
            reverse('habits:habit_update', kwargs={'pk': self.habit.pk}),
            data=data2,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_fail_4_update_habit(self):
        data2 = {
            'location': 'home',
            'time': '14:00',
            'action': 'drink hot water',
            'is_pleasant': True,
            'related_habit': self.related_habit,
            'frequency': datetime.timedelta(hours=100),
            'duration': datetime.timedelta(seconds=100),
            'is_public': False,
        }

        response = self.client.patch(
            reverse('habits:habit_update', kwargs={'pk': self.habit.pk}),
            data=data2,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_habit(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'location': 'home',
            'time': '14:00',
            'action': 'drink hot water',
            'is_pleasant': True,
            'frequency': datetime.timedelta(hours=100),
            'duration': datetime.timedelta(seconds=100),
            'is_public': False,
        }

        response = self.client.post(
            reverse('habits:habit_create'),
            data=data

        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_delete_habit(self):
        response = self.client.delete(
            reverse('habits:habit_delete', kwargs={'pk': self.habit.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class RelatedHabitTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:

        cls.user = User.objects.create(
            email="Test@mail.ru",
            password="Test12345",
            is_active=True,
        )

        cls.related_habit = RelatedHabit.objects.create(
            location='work',
            action='drink coffee',
            duration='80 seconds',
            is_public=True
        )

    def test_create_related_habit(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'location': 'home',
            'action': 'drink hot water',
            'duration': datetime.timedelta(seconds=100),
            'is_public': False,
        }

        response = self.client.post(
            reverse('habits:habit_related_create'),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_update_related_habit(self):
        data2 = {
            'location': 'home',
            'action': 'drink hot water',
            'duration': datetime.timedelta(seconds=70),
            'is_public': False
        }
        response = self.client.put(
            reverse('habits:habit_related_update',
                    kwargs={'pk': self.related_habit.pk}),
            data=data2,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_habit(self):
        response = self.client.delete(
            reverse(
                'habits:habit_related_delete',
                kwargs={'pk': self.related_habit.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
