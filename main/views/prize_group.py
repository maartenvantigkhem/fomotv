from rest_framework import viewsets, filters
from rest_framework.decorators import list_route
from rest_framework.response import Response
from main.models import Prize, PrizeGroup, PrizeGroupRef, Winner
from main.serializers import PrizeGroupRefSerializer


class PrizeGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of prize products.
    """
    queryset = PrizeGroupRef.objects.all()
    serializer_class = PrizeGroupRefSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('group__code', )

    @list_route()
    def winner(self, request):
        code = request.GET.get('code')

        winner = Winner.objects.get(code=code)

        pg_ref = PrizeGroupRef.objects.filter(group=winner.prize_group, prize_type=winner.prize_type)

        serializer = self.get_serializer(pg_ref, many=True)
        return Response(serializer.data)