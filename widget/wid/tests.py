from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Waitlist, Widget

class APITests(APITestCase):
    def test_create_waitlist(self):
        url = reverse('waitlist-create')
        data = {'email': 'stage1@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Waitlist.objects.count(), 1)
        self.assertEqual(Waitlist.objects.get().email, 'stage1@example.com')

    def test_list_widgets(self):
        Widget.objects.create(name='Widget1', description='A widget')
        Widget.objects.create(name='Widget2', description='Another widget')
        url = reverse('widget-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
