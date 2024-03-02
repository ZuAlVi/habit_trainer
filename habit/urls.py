from django.urls import path

from habit.apps import HabitConfig
from habit.views import RelatedHabitCreateApiView, RelatedHabitListApiView, HabitCreateApiView, HabitListApiView, \
    HabitAPIView, HabitUpdateApiView, \
    HabitDestroyApiView

app_name = HabitConfig.name

urlpatterns = [
    path('related_habit/create/', RelatedHabitCreateApiView.as_view(), name='related-habit-create'),
    path('related_habit/list/', RelatedHabitListApiView.as_view(), name='related-habit-list'),
    path('habit/create/', HabitCreateApiView.as_view(), name='habit-create'),
    path('habit/list/', HabitListApiView.as_view(), name='habit-list'),
    path('habit/published/', HabitAPIView.as_view(), name='published-list'),
    path('habit/update/<int:pk>/', HabitUpdateApiView.as_view(), name='habit-update'),
    path('habit/delete/<int:pk>/', HabitDestroyApiView.as_view(), name='habit-delete')
]
