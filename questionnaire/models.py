from django.db import models

# Create your models here.
from django.db.models import Count
from main.models import MyUser, Prize


class Questionnaire(models.Model):
    """
    Questionnaire model

    name - competition name
    image - cover photo
    """
    name = models.CharField(u'Name of Questionnaire', max_length=40)
    title = models.CharField(u'Longer Title', max_length=200)
    image = models.ImageField(u'Background image', upload_to='questionnaire', blank=True, null=True)

    active_flag = models.BooleanField(default=True, verbose_name=u"Is Active")
    top_flag = models.BooleanField(default=False, verbose_name=u"Show on First page")

    author = models.ForeignKey(MyUser, null=True, blank=True, editable=False)

    prizes = models.ManyToManyField(Prize, related_name='questionnaires', through='PrizeQuestionnaireRef')

    end_date = models.DateField(blank=True, null=True)
    end_flag = models.BooleanField(default=False, editable=False)

    @property
    def tagged_name(self):
        return "#" + self.name

    def __unicode__(self):
        return self.name

    @staticmethod
    def get_active():
        questionnaire_list = Questionnaire.objects.filter(top_flag=True, active_flag=True)
        if questionnaire_list.count() == 1:
            return questionnaire_list[0]
        else:
            raise Exception("questionnaire_list not found")

    def get_results(self):
        result_list = QuestionnaireResult.objects.filter(questionnaire=self).annotate(Count('history'))

        all_count = RunHistory.objects.filter(questionnaire=self).count()
        if all_count == 0:
            all_count = 1

        return [{'answer': r.name, 'percent': int(round(float(r.history__count)/all_count*100)), } for r in result_list]


class Question(models.Model):
    """
    Question model
    """
    questionnaire = models.ForeignKey('Questionnaire', related_name='questions')
    title = models.CharField(u'Name', max_length=100)
    image = models.ImageField(u'Background image', upload_to='question', null=True, blank=True)
    sort_id = models.IntegerField(default=0)

    class Meta:
        ordering = ['sort_id', 'title', ]


class QuestionnaireResult(models.Model):
    """
    Possible results of questionnaire depends on "yes" percent
    """
    CODES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    )

    questionnaire = models.ForeignKey('Questionnaire', related_name='results')
    name = models.CharField(max_length=40)
    yes_percent = models.IntegerField()
    result_code =  models.CharField(choices=CODES, max_length=1)


class PrizeQuestionnaireRef(models.Model):
    """
    Many-to-Many relation for Questionnaire-prize with result_code
    """
    questionnaire = models.ForeignKey('Questionnaire')
    prize = models.ForeignKey(Prize)
    result_code = models.CharField(choices=QuestionnaireResult.CODES, max_length=1)


class Answer(models.Model):
    """
    Answer for one question
    """
    questionnaire = models.ForeignKey('Questionnaire')
    question = models.ForeignKey('Question')
    answer = models.IntegerField()
    author = models.ForeignKey(MyUser)


class RunHistory(models.Model):
    """
    For each user, who finished survey, we store finale result of questionnaire run
    """
    author = models.ForeignKey(MyUser)
    questionnaire = models.ForeignKey('Questionnaire', related_name="history")
    #result code base on "yes" stat
    result_code = models.CharField(choices=QuestionnaireResult.CODES, max_length=1)
    result = models.ForeignKey(QuestionnaireResult, null=True, related_name="history")