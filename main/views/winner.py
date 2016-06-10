import json
import urllib
from django.conf import settings
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from main.models import Prize, Winner
from main.serializers import WinnerSerializer


class WinnerViewSet(generics.ListAPIView):
    """
    API endpoint that represents a list of prize products.
    """
    serializer_class = WinnerSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Winner.objects.all()
        code = self.request.query_params.get('code', None)
        if code is not None:
            queryset = queryset.filter(code=code)
        return queryset


@api_view(['POST'])
def confirm(request):
    code = request.POST.get('code')
    prize_id = request.POST.get('prize_id')

    try:
        winner = Winner.objects.get(code=code)
        prize = Prize.objects.get(pk=prize_id)

        if not winner.prize_group.prizes.filter(id=prize.id).exists():
            raise Exception("Prize not found")
    except Exception:
        return Response({
                'status': 'Not found',
                'message': 'Bad winner code or prize id.'
            }, status=status.HTTP_404_NOT_FOUND)

    winner_personal_info = get_winner_info_from_request(request)
    if winner_personal_info['email']:
        winner.prize = prize
        winner.save()

        send_winner_confirmation_email(winner_personal_info['email'], winner_personal_info, prize)

        return Response({
            'status': 'ok'
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'status': 'Not found',
            'message': 'Bad winner info.'
        }, status=status.HTTP_404_NOT_FOUND)


def get_winner_info_from_request(request):
    winner_personal_info = {
        'first_name': request.POST.get('first_name'),
        'last_name': request.POST.get('last_name'),
        'country_code': request.POST.get('country_code'),
        'country_name': request.POST.get('country_name'),
        'zip': request.POST.get('zip'),
        'state': request.POST.get('state'),
        'city': request.POST.get('city'),
        'street': request.POST.get('street'),
        'email': request.POST.get('email'),
        'phone': request.POST.get('phone'),
    }

    return winner_personal_info


def send_winner_confirmation_email(email, details, prize):
    subject, from_email, to_email = u'New prize selection on Prize.tv', \
                                    'products@prized.tv', \
                                    (email, )

    html_data = get_template('email/winner_confirmation.html')

    details['prize_id'] = prize.id
    details['prize_name'] = prize.name

    d = Context(details)
    html_content = html_data.render(d)

    #Send email to site manager
    msg = EmailMessage(subject, html_content, from_email, to=[settings.MANAGER_EMAIL])
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()