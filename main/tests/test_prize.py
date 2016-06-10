import os
from django.test import TestCase
from django.utils.translation import ugettext as _
import json
from rest_framework import status
from main.models import Prize


class PrizeTestCase(TestCase):

    maxDiff = None
    fixtures = ['main/tests/fixtures/competitions.yaml', 'main/tests/fixtures/prizes.yaml', 'main/tests/fixtures/votes.yaml',
                'main/tests/fixtures/winners.yaml',]

    def test_filter_by_group(self):
        prizes = Prize.objects.filter(groups__code='next')
        self.assertEqual(prizes.count(), 2)

    def test_prize_list_by_group(self):
        json_data = open(os.path.dirname(os.path.realpath(__file__)) + '/fixtures/prize_response.json').read()
        expected_prize_list = json.loads(json_data)

        response = self.client.get('/api/v1/prizegroup/?group__code=next')

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(response.content, expected_prize_list)

    def test_prize_list_for_winner(self):
        json_data = open(os.path.dirname(os.path.realpath(__file__)) + '/fixtures/prize_winner_response.json').read()
        expected_prize_list = json.loads(json_data)

        response = self.client.get('/api/v1/prizegroup/winner/?code=8e28bd91-3667-4b65-9ef3-f2f28dac00ec')

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(response.content, expected_prize_list)