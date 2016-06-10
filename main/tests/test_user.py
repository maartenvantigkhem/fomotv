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

    def test_reg(self):
        self.c = Client()
        response = self.c.post('/api/v1/user/', {'email': 'test22@mail.ru', 'password': '1', 'username': 'test22'})

        u = MyUser.objects.get(email='test22@mail.ru')
        self.assertTrue(u.is_active)
        self.assertTrue(u.check_password("1"))
    """
    def test_empty_email(self):
        self.c = Client()
        response = self.c.post('/api/v1/user/', {'email': '', 'password': '1', 'username': 'test22'})

        self.assertEqual(response.status_code, 401)
    """

    def test_bad_email(self):
        self.c = Client()
        response = self.c.post('/api/v1/user/', {'email': 'sss', 'password': '1', 'username': 'test232'})

        self.assertEqual(response.status_code, 400)