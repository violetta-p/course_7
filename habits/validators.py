from rest_framework.exceptions import ValidationError


class DurationValidator:
    def __init__(self, duration):
        self.duration = duration

    def __call__(self, value):
        td_duration = int(dict(value).get(self.duration).total_seconds())
        if int(td_duration) > 120:
            raise ValidationError("Maximum 120 seconds to complete")


class FrequencyValidator:
    def __init__(self, frequency):
        self.frequency = frequency

    def __call__(self, value):
        td_frequency = int(dict(value).get(self.frequency).total_seconds())
        if int(td_frequency) > 604800:
            raise ValidationError("Must be done at least once a week")


class HabitTypeValidator:
    def __init__(self, related_habit, reward, is_pleasant):
        self.related_habit = related_habit
        self.reward = reward
        self.is_pleasant = is_pleasant

    def __call__(self, value):
        related_habit_ = dict(value).get(self.related_habit)
        reward_ = dict(value).get(self.reward)
        is_pleasant_ = dict(value).get(self.is_pleasant)

        if related_habit_ is not None and reward_ is not None:
            raise ValidationError('You can either indicate a related habit '
                                  'or specify a reward')

        if is_pleasant_:
            if related_habit_ is not None or reward_ is not None:
                raise ValidationError('You cannot set a related '
                                      '(pleasant habit as well)'
                                      ' habit or reward for a pleasant habit')
