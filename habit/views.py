from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habit.models import Habit, RelatedHabit
from habit.paginations import ReflexPagination
from habit.serializers import HabitSerializer, RelatedHabitSerializer, HabitDetailSerializer
from users.permissions import IsOwner


class RelatedHabitCreateApiView(generics.CreateAPIView):
    serializer_class = RelatedHabitSerializer

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class RelatedHabitListApiView(generics.ListAPIView):
    serializer_class = RelatedHabitSerializer
    queryset = RelatedHabit.objects.all()


class HabitCreateApiView(generics.CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListApiView(generics.ListAPIView):
    serializer_class = HabitDetailSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitAPIView(generics.ListAPIView):
    serializer_class = HabitDetailSerializer
    queryset = Habit.objects.filter(is_published=True)
    pagination_class = ReflexPagination


class HabitUpdateApiView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Habit.objects.all()


class HabitDestroyApiView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
