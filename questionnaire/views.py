import json
import random
from django.http import HttpResponseBadRequest, HttpResponse
from rest_framework import viewsets, filters
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from main.models import Competition
from main.serializers import CompetitionSerializer
from questionnaire.models import Questionnaire, Question, Answer, QuestionnaireResult, RunHistory
from questionnaire.serializers import QuestionnaireSerializer


class QuestionnaireViewSet(viewsets.ModelViewSet):
    """
    REST API for questionnaire
    """
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('active_flag', 'top_flag', 'end_flag')

    @list_route()
    def top(self, request):
        questionnaire = Questionnaire.get_active()
        serializer = self.get_serializer(questionnaire)
        return Response(serializer.data)

    @list_route()
    def questionnaire_for_user(self, request):
        q = Questionnaire.objects.filter(active_flag=True)
        if request.user.is_authenticated():
            q = q.exclude(history__author=request.user)
        serializer = self.get_serializer(q, many=True)
        return Response(serializer.data)

    @detail_route()
    def result(self, request):
        user = request.user



def save_answer(request):
    """
    save user answer for question
    """
    question_id = request.GET.get('questionId')
    score = request.GET.get('score')

    if not question_id:
        return HttpResponseBadRequest('No question_id')

    if not score:
        return HttpResponseBadRequest('No score')

    if not request.user.is_authenticated():
        return HttpResponseBadRequest('No user')

    question = Question.objects.get(pk=question_id)

    if not question:
        return HttpResponseBadRequest('No question')

    if Answer.objects.filter(question=question)\
        .filter(author=request.user).exists():
        return HttpResponseBadRequest('Already answered')

    if not score.isdigit() or int(score) not in [0, 1]:
        return HttpResponseBadRequest('Bad score')

    v = Answer()
    v.question = question
    v.author = request.user
    v.questionnaire = question.questionnaire
    v.answer = score
    v.save()

    question_count = Question.objects.filter(questionnaire=question.questionnaire).count()
    answer_count = Answer.objects.filter(questionnaire=question.questionnaire, author=request.user).count()

    data = {'finished': False}

    if question_count == answer_count:
        #count yes answers
        yes_count = Answer.objects.filter(questionnaire=question.questionnaire, author=request.user, answer=1).count()
        #count yes percent
        yes_percent = round(float(yes_count)/question_count * 100)
        #select result_code depends on quiz results
        result = QuestionnaireResult.objects.filter(
            yes_percent__lte=yes_percent, questionnaire=question.questionnaire).order_by('-yes_percent')
        if result.count() > 0:
            res = result[0]

            #create RunHistory
            rh = RunHistory()
            rh.author = request.user
            rh.questionnaire = question.questionnaire
            rh.result = res
            rh.result_code = res.name
            rh.save()

            data['results'] = question.questionnaire.get_results()
            data['finished'] = True
            data['user_result'] = res.result_code
            data['win_prize'] = 1 if random.random() < 0.05 else 0
        else:
            #impossible result error
            return HttpResponseBadRequest('Bad result: %d' % yes_percent)

    return HttpResponse(json.dumps(data), content_type='application/json')


def get_result(request):
    questionnaire_id = request.GET.get('questionnaireId')

    if not questionnaire_id:
        return HttpResponseBadRequest('No questionnaire_id')
    questionnaire = Questionnaire.objects.get(pk=questionnaire_id)

    finished = False
    user_result = None
    if request.user.is_authenticated():
        finished = RunHistory.objects.filter(questionnaire=questionnaire, author=request.user).exists()
        if finished:
            r = RunHistory.objects.filter(questionnaire=questionnaire, author=request.user)[0]
            user_result = r.result_code

    data = {
        'finished': finished,
        'user_result': user_result,
        'results': questionnaire.get_results(),
    }
    return HttpResponse(json.dumps(data), content_type='application/json')