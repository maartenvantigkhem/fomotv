"""
Views for user auth
"""

import json

from django.contrib.auth import logout

from rest_framework import permissions, views, status
from rest_framework.response import Response
from social.apps.django_app.default.models import UserSocialAuth
from django.contrib.auth import authenticate, login
from main.serializers import UserSerializer

class LoginView(views.APIView):
    """
    User login via json api
    """
    def post(self, request, format=None):
        
        requestbody = request.body.decode('utf-8')
        body = json.loads(requestbody)

        email = body['email']
        password = body['password']
        
        account = authenticate(email=email, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = UserSerializer(account)
                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)
    


class LogoutView(views.APIView):
    """
    Logout view
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)


class UpdateTermsFlagView(views.APIView):
    """
    Update terms view
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        
        user = request.user
        user.terms_flag = True
        
        user.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


class GetAccessTokenView(views.APIView):
    """
    Get access token for Instagram
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        if request.user.is_authenticated():
            res = UserSocialAuth.objects.filter(user_id=request.user.id).filter(provider='instagram')
            if res.count() > 0:
                params = dict()
                params['access_token'] = res[0].extra_data['access_token']
                return Response(params, status=status.HTTP_200_OK)
        return Response({}, status.HTTP_403_FORBIDDEN)