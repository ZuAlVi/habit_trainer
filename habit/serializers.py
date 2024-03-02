from rest_framework import serializers
from habit.models import Habit, RelatedHabit
from habit.validators import TimeValidator, HabitFeeValidator, HabitPleasantValidator


class RelatedHabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = RelatedHabit
        fields = '__all__'


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [TimeValidator("time_to_complete"),
                      HabitPleasantValidator("is_pleasant", "related_habit", "fee"),
                      HabitFeeValidator('related_habit', 'fee')
                      ]


class HabitDetailSerializer(serializers.ModelSerializer):
    habit = HabitSerializer(read_only=True)

    class Meta:
        model = Habit
        fields = '__all__'
