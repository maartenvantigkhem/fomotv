from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf.urls import patterns
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from main.views.auth import LogoutView, GetAccessTokenView, UpdateTermsFlagView, LoginView
from main.views.categories import CategoryViewSet
from main.views.competition import CompetitionViewSet
from main.views.photos import PhotoViewSet
from main.views.prize import PrizesViewSet
from main.views.trends import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles import views
from main.views.prize_group import PrizeGroupViewSet
from main.views.user import UserViewSet
from main.views.winner import WinnerViewSet

admin.autodiscover()

router = routers.SimpleRouter()
router.register(r'prizes', PrizesViewSet, base_name='prizes')
router.register(r'prizegroup', PrizeGroupViewSet, base_name='prizegroup')
router.register(r'photos', PhotoViewSet, base_name='photos')
router.register(r'competitions', CompetitionViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'user', UserViewSet)
router.register(r'colortrend', ColorTrendViewSet)
router.register(r'designtrendphotos', DesignTrendPhotosViewSet)
router.register(r'designsizestrend', DesignSizesTrendViewSet)
router.register(r'designavailablecolors', DesignTrendAvailableColorsViewSet)
router.register(r'useridtrend', UserIDTrendViewSet)
router.register(r'designtrend', DesignTrendViewSet)
router.register(r'uservotingtrend', UserVotingTrendViewSet)

urlpatterns = [
    url(r'^$', 'main.views.common.index', name='home'),
    url(r'^upload_photo_by_url/$', 'main.views.common.upload_photo_by_url', name='upload_photo_by_url'),
    url(r'^upload_photo_from_src/$', 'main.views.common.upload_photo_from_src', name='upload_photo_from_src'),
    url(r'^ajax-auth/(?P<backend>[^/]+)/$', 'main.views.common.ajax_auth',
        name='ajax-auth'),

    url(r'^photo/vote$', 'main.views.vote.vote', name='vote'),
    url(r'^photo/share$', 'main.views.vote.share', name='share'),

    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^api/v1/auth/update-terms-flag/$', UpdateTermsFlagView.as_view(), name='update-terms-flag'),
    url(r'^api/v1/file-upload/$', 'main.views.common.upload_photo_from_file', name='file-upload'),
    url(r'^api/v1/auth/get-access-token/$', GetAccessTokenView.as_view(), name='get_access_token'),
    url(r'^api/v1/winner/$', WinnerViewSet.as_view(), name='winner'),
    url(r'^api/v1/winner/confirm/$', 'main.views.winner.confirm', name='winner_confirm'),

    url(r'^admin/', include(admin.site.urls)),

    url('^order/', include('order.urls', namespace='order')),
    url('', include('questionnaire.urls', namespace='questionnaire')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social.apps.django_app.urls', namespace='social')),
]

if settings.DEBUG:
    #print BASE_DIR
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += staticfiles_urlpatterns()