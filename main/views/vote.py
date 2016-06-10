"""
Vote and Share function for photos
TODO: move to photo REST API
"""
import json
from django.db.models import Q
from django.http import HttpResponse, HttpResponseBadRequest
from main.models import Competition, Photo, VoteHistory, ViewHistory


def vote(request):
    """
    Vote action
    """
    photo_id = request.GET.get('photoId')
    score = request.GET.get('score')
    competition_id = request.GET.get('competitionId')

    if not photo_id:
        return HttpResponseBadRequest('No photo')

    if not score:
        return HttpResponseBadRequest('No score')

    if not request.user.is_authenticated():
        return HttpResponseBadRequest('No user')

    photo = Photo.objects.get(pk=photo_id)

    if not photo:
        return HttpResponseBadRequest('No photo')

    if not competition_id:
        return HttpResponseBadRequest('No competition')

    competition = Competition.objects.get(pk=competition_id)

    if not ViewHistory.objects.filter(photo=photo, from_user=request.user).exists():
        view = ViewHistory()
        view.competition = competition
        view.from_user = request.user
        view.photo = photo
        view.save()

    if VoteHistory.objects.filter(photo=photo)\
        .filter(Q(from_user=request.user) | Q(session=request.session.session_key)).exists():
        return HttpResponseBadRequest('Already voted')

    if not score.isdigit() or int(score) not in [0, 1]:
        return HttpResponseBadRequest('Bad score')

    v = VoteHistory()
    v.competition = competition
    v.from_user = request.user
    v.to_user = photo.author
    v.photo = photo
    v.vote_count = score
    v.vote_type = VoteHistory.VOTE_TYPE
    v.session = request.session.session_key
    v.save()



    data = {'ok': 1}
    return HttpResponse(json.dumps(data), content_type='application/json')


def share(request):
    """

    """
    photo_id = request.GET.get('photoId')
    competition_id = request.GET.get('competitionId')

    if not photo_id:
        return HttpResponseBadRequest('No photo')

    photo = Photo.objects.get(pk=photo_id)

    if not photo:
        return HttpResponseBadRequest('No photo')

    if not competition_id:
        return HttpResponseBadRequest('No competition')

    competition = Competition.objects.get(pk=competition_id)

    if VoteHistory.objects.filter(photo=photo)\
        .filter(Q(from_user=request.user) | Q(session=request.session.session_key)).exists():
        return HttpResponseBadRequest('Already voted')

    v = VoteHistory()
    v.competition = competition
    v.from_user = request.user
    v.to_user = photo.author
    v.photo = photo
    v.vote_count = 10
    v.vote_type = VoteHistory.SHARE_TYPE
    v.session = request.session.session_key
    v.save()

    v = VoteHistory()
    v.competition = competition
    v.from_user = request.user
    v.to_user = request.user
    v.photo = photo
    v.vote_count = 10
    v.vote_type = VoteHistory.SHARE_TYPE
    v.session = request.session.session_key
    v.save()

    data = {'ok': 1}
    return HttpResponse(json.dumps(data), content_type='application/json')
