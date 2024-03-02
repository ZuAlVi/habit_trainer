from django.contrib import admin

from habit.models import Habit, RelatedHabit


@admin.register(RelatedHabit)
class RelatedHabitAdmin(admin.ModelAdmin):
    list_display = ('id', 'activity')


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('id', 'activity')
