"""
Rest framework serializers
"""
from main.serializers import ProductPhotoSerializer, ProductColorSerializer
from models import Questionnaire, Question, PrizeQuestionnaireRef
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    """
    Question serializer
    """
    class Meta:
        model = Question
        fields = ('id', 'title', 'image', 'sort_id', )


class PrizeQuestionnaireSerializer(serializers.HyperlinkedModelSerializer):
    """
    serialize all prize fields
    """
    id = serializers.ReadOnlyField(source='prize.id')
    questionnaire_id = serializers.ReadOnlyField(source='questionnaire.id')
    name = serializers.ReadOnlyField(source='prize.name')
    thumbnail = serializers.ImageField(source='prize.thumbnail')
    discount_amount = serializers.ReadOnlyField(source='prize.discount_amount')
    sale_price = serializers.ReadOnlyField(source='prize.sale_price')
    retail_price = serializers.ReadOnlyField(source='prize.retail_price')
    hover_description = serializers.ReadOnlyField(source='prize.hover_description')
    description = serializers.ReadOnlyField(source='prize.description')

    photos = ProductPhotoSerializer(source='prize.photos', many=True, read_only=True)
    colors = ProductColorSerializer(source='prize.colors', many=True, read_only=True)
    sizes = serializers.ListField(source='prize.sizes',
        child=serializers.CharField()
    )

    class Meta:
        model = PrizeQuestionnaireRef
        fields = ('result_code', 'id', 'questionnaire_id', 'name', 'thumbnail',
                  'discount_amount', 'sale_price', 'retail_price', 'hover_description',
                  'photos', 'colors', 'sizes', 'description',
        )


class QuestionnaireSerializer(serializers.ModelSerializer):
    """
    Questionnaire serializer
    """
    prizes = PrizeQuestionnaireSerializer(source="prizequestionnaireref_set", many=True, read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Questionnaire
        fields = ('id', 'name', 'title', 'image', 'prizes', 'active_flag', 'top_flag', 'questions', 'end_date', )
