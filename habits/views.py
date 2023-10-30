from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habits.models import Habit, RelatedHabit
from habits.paginators import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer, RelatedHabitSerializer
from datetime import timedelta

class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    #permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator

    def get_queryset(self):
        user = self.request.user
        queryset = Habit.objects.filter(user=user.id)
        return queryset


class PublicHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    #permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator

    def get_queryset(self):
        queryset = Habit.objects.filter(is_public=True)
        return queryset


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    #permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    #permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    #permission_classes = [IsAuthenticated, IsOwner]


class RelatedHabitCreateAPIView(generics.CreateAPIView):
    serializer_class = RelatedHabitSerializer
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class RelatedHabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = RelatedHabitSerializer
    queryset = RelatedHabit.objects.all()
    #permission_classes = [IsAuthenticated, IsOwner]


class RelatedHabitDestroyAPIView(generics.DestroyAPIView):
    queryset = RelatedHabit.objects.all()
    #permission_classes = [IsAuthenticated, IsOwner]
