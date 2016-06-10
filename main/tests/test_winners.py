import datetime
from django.core import mail
from django.test import TestCase, Client
from main.models import VoteHistory, Competition, Winner, Prize, PrizeGroup
from main.winner import get_top_voter, get_best_photo, set_winners, update_competition_prizes, send_winner_email


class WinnerTestCase(TestCase):

    maxDiff = None
    fixtures = ['main/tests/fixtures/competitions.yaml', 'main/tests/fixtures/prizes.yaml',
                'main/tests/fixtures/votes.yaml', 'main/tests/fixtures/config.yaml',
                'main/tests/fixtures/winners.yaml']

    winner_info = {
            'code': "8e28bd91-3667-4b65-9ef3-f2f28dac00ec",
            'prize_id': '1',
            'first_name': "test",
            'last_name':  "test",
            'country_code':  "test",
            'country_name':  "test",
            'street':  "test",
            'city':  "test",
            'state':  "test",
            'zip':  "test",
            'email': "test",
            'phone': "test",
        }

    def test_vote_count(self):
        c = VoteHistory.objects.count()
        self.assertEqual(c, 4)

    def test_random_winner(self):
        current_date = datetime.date(2015, 10, 18)
        competition = Competition.objects.get(pk=1)

        from_date = current_date - datetime.timedelta(days=8)
        #to_date = current_date - datetime.timedelta(days=8)

        min_user_id = 0

        winner = get_top_voter(competition, min_user_id, from_date, current_date)

        self.assertEqual(winner, 2)

    def test_best_photo(self):
        current_date = datetime.date(2015, 10, 18)
        competition = Competition.objects.get(pk=1)

        from_date = current_date - datetime.timedelta(days=8)

        min_user_id = 0

        best_photo = get_best_photo(competition, min_user_id, from_date, current_date)

        self.assertEqual(best_photo, 2)

    def test_winner_record_create(self):
        current_date = datetime.date(2015, 10, 21)

        self.assertEqual(current_date.weekday(), 2)

        set_winners(current_date)

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 4)

        winners = Winner.objects.all()
        self.assertEqual(winners.count(), 3)

    def test_update_prizes(self):
        prizes = Prize.objects.filter(groups__code='next')
        self.assertEqual(prizes.count(), 2)

        current_date = datetime.date(2015, 10, 18)
        update_competition_prizes(current_date)

        prizes = Prize.objects.filter(groups__code='next')
        self.assertEqual(prizes.count(), 0)

    def test_week_day_config_bad_day(self):
        current_date = datetime.date(2015, 10, 18)

        self.assertEqual(current_date.weekday(), 6)

        set_winners(current_date)

        winners = Winner.objects.all()
        self.assertEqual(winners.count(), 1) # no new winners

    def test_old_prev_prize_group(self):
        current_date = datetime.date(2015, 10, 21)

        set_winners(current_date)

        self.assertTrue(PrizeGroup.objects.filter(code="history-2015-10-21").exists())

        prizes = Prize.objects.filter(groups__code='history-2015-10-21')
        self.assertEqual(prizes.count(), 2)

        pg = PrizeGroup.objects.get(code="history-2015-10-21")
        self.assertEqual(pg.winners.count(), 2)

    def test_winner_confirmation(self):
        self.c = Client()
        #response = self.c.post('/api/v1/auth/login/', {'email': 'test1@mail.ru', 'password': '1'})

        response = self.c.post('/api/v1/winner/confirm/', self.winner_info)
        self.assertEquals(response.status_code, 200)

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, u'New prize selection on Prize.tv')

        self.assertTrue(u"<td>First Name</td><td>test</td>" in mail.outbox[0].body)
        self.assertTrue(u'<a href="http://prized.tv/#!/prize/1/" >Product test 1</a>' in mail.outbox[0].body)

        winner = Winner.objects.get(code=self.winner_info['code'])
        self.assertEqual(winner.prize_id, 1)

    def test_winner_confirmation_no_code(self):
        self.c = Client()
        #response = self.c.post('/api/v1/auth/login/', {'email': 'test1@mail.ru', 'password': '1'})

        self.winner_info['code'] = "bad"

        response = self.c.post('/api/v1/winner/confirm/', self.winner_info)
        self.assertEquals(response.status_code, 404)

    def test_winner_confirmation_bad_prize(self):
        self.c = Client()
        #response = self.c.post('/api/v1/auth/login/', {'email': 'test1@mail.ru', 'password': '1'})

        self.winner_info['prize_id'] = 3

        response = self.c.post('/api/v1/winner/confirm/', self.winner_info)
        self.assertEquals(response.status_code, 404)

    def test_winner_email_send(self):
        email = "test@mail.ru"
        code = "123456"

        send_winner_email(email, code, 'email/winner_top_voter.html')

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 2)

        # Verify that the subject of the first message is correct.
        self.assertTrue(code in mail.outbox[0].body)






