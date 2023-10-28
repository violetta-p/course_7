from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitListAPIView, PublicHabitListAPIView, HabitRetrieveAPIView, \
    HabitUpdateAPIView, HabitDestroyAPIView, RelatedHabitCreateAPIView, RelatedHabitUpdateAPIView, \
    RelatedHabitDestroyAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit/', HabitListAPIView.as_view(), name='habit_list'),
    path('habit/published/', PublicHabitListAPIView.as_view(), name='public_habit_list'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_get'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
    path('habit/related/create/', RelatedHabitCreateAPIView.as_view(), name='habit_related_create'),
    path('habit/related/update/<int:pk>/', RelatedHabitUpdateAPIView.as_view(), name='habit_related_update'),
    path('habit/related/delete/<int:pk>/', RelatedHabitDestroyAPIView.as_view(), name='habit_related_delete'),
]
