from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from habit.models import Habit, RelatedHabit
from users.models import User


class RelatedHabitTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='test@test.com',
            password='1111'
        )
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_related_habit_create(self):
        data = {
            'user': self.user.pk,
            'activity': 'some',
        }
        response = self.client.post(reverse('habit:related-habit-create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_related_habit_list(self):
        RelatedHabit.objects.create(
            user=self.user, activity='some 2'
        )
        response = self.client.get(reverse('habit:related-habit-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json(),
            [{'id': 2, 'activity': 'some 2', 'user': 7}])


class HabitTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='test@test.com',
            password='1111'
        )
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        data = {
            "periodicity": 'week',
            'user': self.user.id,
            'fee': 'test',
            'time_to_complete': 12,
            'activity': 'test',
            'usual_time': '2022-03-02',
            'place': 'test'
        }
        response = self.client.post(reverse('habit:habit-create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_habit_list(self):
        Habit.objects.create(
            periodicity='week',
            user=self.user,
            fee='test',
            time_to_complete=12,
            activity='test',
            usual_time='2022-03-02',
            place='test'

        )
        response = self.client.get(reverse('habit:habit-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json(),
            [{'id': 3, 'related_habit': None, 'periodicity': 'week', 'is_published': False, 'is_pleasant': False,
              'fee': 'test', 'time_to_complete': 12, 'activity': 'test', 'usual_time': '2022-03-02T00:00:00Z',
              'place': 'test', 'user': 3}]
        )

    def test_habit_delete(self):
        habit = Habit.objects.create(
            periodicity='week',
            user=self.user,
            fee='test',
            time_to_complete=12,
            activity='test',
            usual_time='2022-03-02',
            place='test'
        )
        url = f'/habit/delete/{habit.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_habit_published_list(self):
        Habit.objects.create(
            periodicity='week',
            is_published=True,
            user=self.user,
            fee='test',
            time_to_complete=12,
            activity='test',
            usual_time='2022-03-02',
            place='test'

        )
        response = self.client.get(reverse('habit:published-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': 4, 'related_habit': None, 'periodicity': 'week', 'is_published': True, 'is_pleasant': False,
                 'fee': 'test', 'time_to_complete': 12, 'activity': 'test', 'usual_time': '2022-03-02T00:00:00Z',
                 'place': 'test', 'user': 4}]})

    def test_habit_update(self):

        habit = Habit.objects.create(
            periodicity='week',
            user=self.user,
            fee='test',
            time_to_complete=12,
            activity='test',
            usual_time='2021-01-01',
            place='test'
        )
        updated_data = {
            'periodicity': 'week',
            'fee': 'updated_fee',
            'time_to_complete': 15,
            'activity': 'updated_activity',
            'usual_time': '2022-02-13',
            'place': 'updated_place'
        }

        url = f'/habit/update/{habit.id}/'
        response = self.client.patch(url, data=updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
