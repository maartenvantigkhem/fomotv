from rest_framework import viewsets
from main.models import ColorTrend, DesignTrend
from main.models import DesignTrendPhotos, DesignSizesTrend
from main.models import UserIDTrend, UserVotingTrend, DesignTrendAvailableColors
from main.serializers import ColorTrendSerializer, DesignTrendSerializer
from main.serializers import DesignTrendPhotosSerializer, DesignSizesTrendSerializer
from main.serializers import UserIDTrendSerializer, UserVotingTrendSerializer
from main.serializers import DesignTrendAvailableColorsSerializer
from rest_framework.decorators import list_route, detail_route
import itertools


class ColorTrendViewSet(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of colors in the color Trends.
    """
    serializer_class = ColorTrendSerializer
    queryset = ColorTrend.objects.all()


class DesignTrendViewSet(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of colors in the color Trends.
    """
    serializer_class = DesignTrendSerializer
    queryset = DesignTrend.objects.all()


class DesignTrendPhotosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of colors in the color Trends.
    """
    serializer_class = DesignTrendPhotosSerializer
    queryset = DesignTrendPhotos.objects.all()


class DesignSizesTrendViewSet(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of colors in the color Trends.
    """
    serializer_class = DesignSizesTrendSerializer
    queryset = DesignSizesTrend.objects.all()


class UserIDTrendViewSet(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of colors in the color Trends.
    """
    serializer_class = UserIDTrendSerializer
    queryset = UserIDTrend.objects.all()


class DesignTrendAvailableColorsViewSet(viewsets.ModelViewSet):

    serializer_class = DesignTrendAvailableColorsSerializer
    queryset = DesignTrendAvailableColors.objects.all()


class UserVotingTrendViewSet(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of colors in the color Trends.
    """
    serializer_class = UserVotingTrendSerializer
    queryset = UserVotingTrend.objects.all()


