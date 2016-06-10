"""
1. create prize history for every competition
2. unique code for every type of prize
3. email with prize link
4. page with prizes of one type (bp, bv)

"""
import os
import random
import sys
import datetime

sys.path.insert(0, "/var/www/uwsgi/fomotv/src")
sys.path.insert(0, "/var/www/fomotv.net/fomotv/src")

from django.db import connection
from django.conf import settings
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from main.models import Competition, Photo, Winner, Prize, MyUser, PrizeGroup, PrizeGroupRef, Config


def send_winner_email(email, code, template):
    subject, from_email, to_email = u'Congratulations! Your this week\'s winner', \
                                    'products@prized.tv', \
                                    (email, )

    html_data = get_template(template)

    d = Context({
        'code': code
    })

    html_content = html_data.render(d)
    msg = EmailMessage(subject, html_content, from_email, to_email)
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()

    msg = EmailMessage('Competition winner on Prized.tv', html_content, 'products@prized.tv', (settings.MANAGER_EMAIL,))
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()


def get_top_voter(c, min_user_id, from_date, to_date):
    sql = "SELECT from_user_id, sum(vote_count) all_vote_count FROM `main_votehistory` WHERE `competition_id` = %d " \
              "and from_user_id > %d and create_date between '%s' and '%s'" \
              "group by from_user_id order by all_vote_count limit 1" % \
          (c.id, min_user_id, from_date.strftime("%Y-%m-%d"), to_date.strftime("%Y-%m-%d"))

    cursor = connection.cursor()
    cursor.execute(sql)
    winner = cursor.fetchone()

    if winner and len(winner) > 0:
        return winner[0]
    else:
        return None


def get_best_photo(c, min_user_id, from_date, to_date):
    sql = """
            SELECT p.id, sum(v.vote_count) vc FROM `main_votehistory` v, main_photo p
            WHERE p.author_id > %d and v.`competition_id` = %d and p.id = v.photo_id and p.active_flag=1
            and p.create_date between '%s' and '%s'
            group by p.id
            order by vc desc limit 1
        """ % (min_user_id, c.id, from_date, to_date)

    cursor = connection.cursor()
    cursor.execute(sql)
    winner = cursor.fetchone()

    if winner and len(winner) > 0:
        return winner[0]
    else:
        return None


def update_competition_prizes(current_date):
    #remove prizes from prev group
    #move from current to prev
    #move from next to current

    #pg_prev = PrizeGroup.objects.get(code='previous')
    pg_current = PrizeGroup.objects.get(code='current')

    #create old prize group archive for winners
    pg_old = PrizeGroup()
    pg_old.name = "%s %s" % ("History", current_date.strftime("%Y-%m-%d"))
    pg_old.code = "%s-%s" % ("history", current_date.strftime("%Y-%m-%d"))
    pg_old.save()

    pg_next = PrizeGroup.objects.get(code='next')

    PrizeGroupRef.objects.filter(group=pg_current).update(group=pg_old)
    PrizeGroupRef.objects.filter(group=pg_next).update(group=pg_current)

    return pg_old


def set_winners(current_date):

    config = Config.objects.get(pk=1)

    if int(config.refresh_week_day) != current_date.weekday()+1:
        return False

    from_date = current_date - datetime.timedelta(days=8)

    competition_list = Competition.objects.filter(active_flag=True)

    max_admin_user_id = 30
    max_admin_user_id = 0

    pg_old = update_competition_prizes(current_date)

    for c in competition_list:
        top_voter_id = get_top_voter(c, max_admin_user_id, from_date, current_date)

        if top_voter_id:
            w = Winner()
            w.competition = c
            w.user_id = top_voter_id
            w.prize_type = Prize.RANDOM_VOTE
            w.prize_group = pg_old
            w.save()

            user = MyUser.objects.get(pk=top_voter_id)
            if user.email:
                send_winner_email(user.email, w.code, 'email/winner_top_voter.html')

        best_photo_id = get_best_photo(c, max_admin_user_id, from_date, current_date)

        if best_photo_id:
            photo = Photo.objects.get(pk=best_photo_id)

            w = Winner()
            w.competition = c
            w.photo = photo
            w.user = photo.author
            w.prize_type = Prize.BEST_PHOTO
            w.prize_group = pg_old
            w.save()

            if photo.author.email:
                send_winner_email(photo.author.email,  w.code, 'email/winner_best_photo.html')
