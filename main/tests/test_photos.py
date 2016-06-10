import os
from django.test import TestCase, Client
from django.utils.translation import ugettext as _
import json
from rest_framework import status
from main.models import Prize, MyUser


class PhotoTestCase(TestCase):

    maxDiff = None
    fixtures = ['main/tests/fixtures/competitions.yaml', 'main/tests/fixtures/prizes.yaml',
                'main/tests/fixtures/votes.yaml',
                'main/tests/fixtures/winners.yaml',]


    def test_history_clean(self):
        u = MyUser.objects.get(email='test1@mail.ru')
        self.assertTrue(u.is_active)
        self.assertTrue(u.check_password("1"))

        self.c = Client()
        response = self.c.post('/api/v1/auth/login/', {'email': 'test1@mail.ru', 'password': '1'})
        self.assertEquals(response.status_code, 200)

        response = self.c.get('/api/v1/photos/?competition_id=1')
        photos = json.loads(response.content)['results']
        self.assertEqual(len(photos), 1)

        response = self.c.get('/api/v1/competitions/1/clean_view_history/')

        response = self.c.get('/api/v1/photos/?competition_id=1')
        photos = json.loads(response.content)['results']
        self.assertEqual(len(photos), 3)
