from django.conf.urls import patterns, url, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'questionnaire', views.QuestionnaireViewSet)

urlpatterns = patterns(
    '',
    url(r'^api/v1/', include(router.urls)),
    url(r'^questionnaire/save_answer$', 'questionnaire.views.save_answer', name='save_answer'),
    url(r'^questionnaire/get_result$', 'questionnaire.views.get_result', name='get_result$'),
)