from rest_framework import viewsets, filters
from main.models import Prize
from main.serializers import PrizeSerializer


class PrizesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of prize products.
    """
    serializer_class = PrizeSerializer

    def get_queryset(self):
        """
        Optional filtering by group code
        """
        queryset = Prize.objects.all()
        group_code = self.request.query_params.get('group_code', None)
        if group_code is not None:
            queryset = queryset.filter(groups__code=group_code)
        return queryset