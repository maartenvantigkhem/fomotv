"""
Views for user registration
"""
import json

from rest_framework import permissions, status, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from main.models import MyUser
from main.permissions import IsAccountOwner
from main.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    parser_classes = (JSONParser,)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request, *args, **kwargs):
        requestbody = request.body.decode('utf-8')
        body = json.loads(requestbody)

        email = body['email']
        password = body['password']
        username = body['username']

        data = {'email': email, 'password': password, 'username': username}
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            MyUser.objects.create_user(**serializer.validated_data)
            return Response(
                serializer.validated_data, status=status.HTTP_201_CREATED
                )

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_404_NOT_FOUND)
