"""
REST API for competitions
"""
from rest_framework import viewsets, filters
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from main.models import Competition, ViewHistory
from main.serializers import CompetitionSerializer


class CompetitionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of cometitions.
    """
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('active_flag', 'top_flag', 'end_flag')

    @list_route()
    def top(self, request):
        competition = Competition.get_active()
        serializer = self.get_serializer(competition)
        return Response(serializer.data)

    @detail_route()
    def clean_view_history(self, request, pk=None):
        competition = Competition.objects.get(pk=pk)

        if request.user.is_authenticated():
            ViewHistory.objects.filter(from_user=request.user, competition=competition).delete()
            return Response({'ok': 1})
        else:
            return Response({'error': 1})