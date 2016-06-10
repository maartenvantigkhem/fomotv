"""
REST API for competition photos
"""
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route, list_route
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from main.models import Photo
from main.serializers import PhotoSerializer


class PhotoPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = None


class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of competition photos
    """
    serializer_class = PhotoSerializer
    pagination_class = PhotoPagination

    def get_queryset(self):
        """
        custom queryset for competition photos list
        filter by active_flag, competition_id, users vote history
        """
        user = self.request.user

        competition_id = self.request.GET.get('competition_id', 0)
        photos = Photo.objects.filter(competition_id=competition_id, active_flag=True)

        if user.is_authenticated():
            photos = photos.exclude(view_history__from_user=user)

        photos = list(photos)

        photo_id = self.request.GET.get('photo_id', 0)
        top_photo = Photo.objects.filter(pk=photo_id, active_flag=True)
        if top_photo.count() == 1:
            photos.insert(0, top_photo[0])

        return photos


    @detail_route()
    def abuse(self, request, pk=None):
        """
        Action for abuse reporting
        type - abuse type
        pk - photo id in DB
        """
        abuse_type = self.request.GET.get('type', '')

        p = Photo.objects.filter(pk=pk)
        if p.count() == 1:
            photo = p[0]
            photo.active_flag = False
            photo.spam_flag = True
            print [t[0] for t in Photo.ABUSE_TYPES]
            if abuse_type in [t[0] for t in Photo.ABUSE_TYPES]:
                photo.abuse_reason = abuse_type
            photo.save()

            return Response({'success': True}, status=status.HTTP_200_OK)
        else:
            return Response({'message':'photo not found'}, status=status.HTTP_404_NOT_FOUND)