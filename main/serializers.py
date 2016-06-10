"""
Rest framework serializers
"""
from django.contrib.auth import update_session_auth_hash
from models import Prize, ProductPhoto, Competition, ProductColor, Photo
from models import PrizeCompetitionRef, Category, Winner, MyUser, PrizeGroupRef
from models import ColorTrend, DesignTrend, DesignSizesTrend, DesignTrendPhotos
from models import UserVotingTrend, UserIDTrend, DesignTrendAvailableColors
from rest_framework import serializers


class DesignTrendPhotosSerializer(serializers.ModelSerializer):
    """
    Serialize the Desgin Trend Model
    """

    class Meta:
        model = DesignTrendPhotos
        fields = ('design_photos',)


class UserVotingTrendSerializer(serializers.ModelSerializer):
    """
    Serialize the Desgin Trend Model
    """

    class Meta:
        model = UserVotingTrend


class UserIDTrendSerializer(serializers.ModelSerializer):
    """
    Serialize the Desgin Trend Model
    """

    class Meta:
        model = UserIDTrend


class DesignSizesTrendSerializer(serializers.ModelSerializer):
    """
    Serialize the Desgin Trend Model
    """

    class Meta:
        model = DesignSizesTrend
        fields = ('sizes',)


class ColorTrendSerializer(serializers.ModelSerializer):
    """
    Serialize the Color Trend Model
    """

    class Meta:
        model = ColorTrend
        fields = ('color_name', 'color_hex', 'up_votes', 'down_votes')


class DesignTrendAvailableColorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DesignTrendAvailableColors
        fields = ('design_colors', )


class DesignTrendSerializer(serializers.ModelSerializer):
    """
    Serialize the Desgin Trend Model
    """

    photos = DesignTrendPhotosSerializer(many=True)
    sizes = DesignSizesTrendSerializer(many=True)
    colors = DesignTrendAvailableColorsSerializer(many=True)

    class Meta:
        model = DesignTrend


class UserSerializer(serializers.ModelSerializer):
    """
    serialize User model
    """

    # The password and the confirm_password are mentioned
    # separately and not as a part of the
    # 'fields' below because we want to be able to mention
    # required=False. All the items mentioned
    # int the fields are required. But we dont want to change the password
    # everytime, unless it has
    # been updated by the user.  --Vik.

    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = MyUser
        fields = ('id', 'email', 'username',
                  'first_name', 'last_name', 'password',
                  'confirm_password',)

        def create(self, validated_data):
            return MyUser.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)
            instance.save()

            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)

            if password and confirm_password and password == confirm_password:
                instance.set_password(password)
                instance.save()

            update_session_auth_hash(self.context.get('request'), instance)

            return instance


class ProductPhotoSerializer(serializers.ModelSerializer):
    """
    serialize Product Photo
    """

    class Meta:
        model = ProductPhoto
        fields = ('id', 'image')


class ProductColorSerializer(serializers.ModelSerializer):
    """
    serialize Product Colors
    """

    class Meta:
        model = ProductColor
        fields = ('id', 'name', 'color_code')


class PrizeSerializer(serializers.ModelSerializer):
    """
    serialize all prize fields
    """
    photos = ProductPhotoSerializer(many=True, read_only=True)
    colors = ProductColorSerializer(many=True, read_only=True)
    sizes = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Prize
        fields = ('id', 'name', 'thumbnail', 'retail_price', 'photos', 'colors', 'description',
                  'size_type', 'sale_price', 'discount_amount', 'sizes')


class PhotoSerializer(serializers.ModelSerializer):
    """
    serialize users Photo
    """

    class Meta:
        model = Photo
        fields = ('id', 'image')


class WinnerSerializer(serializers.ModelSerializer):
    """
    Competition winners history serializer
    """
    photo = PhotoSerializer()
    user = UserSerializer()

    class Meta:
        model = Winner
        fields = ('user', 'photo', 'prize_type', 'code', 'prize')


class PrizeCompetitionSerializer(serializers.HyperlinkedModelSerializer):
    """
    serialize all prize fields
    """
    id = serializers.ReadOnlyField(source='prize.id')
    competition_id = serializers.ReadOnlyField(source='competition.id')
    name = serializers.ReadOnlyField(source='prize.name')
    thumbnail = serializers.ImageField(source='prize.thumbnail')
    discount_amount = serializers.ReadOnlyField(source='prize.discount_amount')
    sale_price = serializers.ReadOnlyField(source='prize.sale_price')
    retail_price = serializers.ReadOnlyField(source='prize.retail_price')
    hover_description = serializers.ReadOnlyField(source='prize.hover_description')
    description = serializers.ReadOnlyField(source='prize.description')
    size_type = serializers.ReadOnlyField(source='prize.size_type')

    photos = ProductPhotoSerializer(source='prize.photos', many=True, read_only=True)
    colors = ProductColorSerializer(source='prize.colors', many=True, read_only=True)
    sizes = serializers.ListField(source='prize.sizes',
                                  child=serializers.CharField()
    )

    class Meta:
        model = PrizeCompetitionRef
        fields = ('prize_type', 'id', 'competition_id', 'name', 'thumbnail',
                  'discount_amount', 'sale_price', 'retail_price', 'hover_description',
                  'photos', 'colors', 'sizes', 'description', 'size_type'
        )


class PrizeGroupRefSerializer(PrizeCompetitionSerializer):
    class Meta:
        model = PrizeGroupRef
        fields = ('prize_type', 'id', 'competition_id', 'name', 'thumbnail',
                  'discount_amount', 'sale_price', 'retail_price', 'hover_description',
                  'photos', 'colors', 'sizes', 'description', 'size_type'
        )


class CompetitionSerializer(serializers.ModelSerializer):
    """
    Competition serializer
    """
    prizes = PrizeCompetitionSerializer(source="prizecompetitionref_set", many=True, read_only=True)
    winners = WinnerSerializer(many=True, read_only=True)

    class Meta:
        model = Competition
        fields = ('id', 'name', 'image', 'description', 'prizes', 'active_flag', 'top_flag', 'winners', 'end_date', )


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for product categories
    """
    children = RecursiveField(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'depth', 'children', 'path', )
