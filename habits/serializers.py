from rest_framework import serializers

from habits.models import Habit, RelatedHabit
from habits.validators import DurationValidator, \
    HabitTypeValidator, FrequencyValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [DurationValidator(duration='duration'),
                      FrequencyValidator(frequency='frequency'),
                      HabitTypeValidator(related_habit='related_habit',
                                         reward='reward',
                                         is_pleasant='is_pleasant'),
                      ]


class RelatedHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedHabit
        fields = '__all__'
        validators = [DurationValidator(duration='duration')]
