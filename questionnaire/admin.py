from django.contrib import admin
from questionnaire.models import Question, Questionnaire, PrizeQuestionnaireRef, QuestionnaireResult


class PrizeQuestionnaireInline(admin.TabularInline):
    model = PrizeQuestionnaireRef
    extra = 1


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class QuestionnaireResultInline(admin.TabularInline):
    model = QuestionnaireResult
    extra = 1


class QuestionnaireAdmin(admin.ModelAdmin):
    """
    Settings for Competition Admin Section
    """
    list_display = ['name', 'active_flag', 'top_flag', 'id', 'admin_thumbnail']
    inlines = [QuestionInline, QuestionnaireResultInline, PrizeQuestionnaireInline]

    def admin_thumbnail(self, obj):
        return u'<img src="%s" width="50"/>' % (obj.image.url) if obj.image else ""
    admin_thumbnail.short_description = 'Background Image'
    admin_thumbnail.allow_tags = True

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

admin.site.register(Questionnaire, QuestionnaireAdmin)