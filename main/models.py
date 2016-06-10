"""
Django models
"""
import random
import string
import datetime
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core import validators
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from select_multiple_field.models import SelectMultipleField
from treebeard.mp_tree import MP_Node

"""
ALl models that end with the word Trend are used only for MarketResearch Study
and are not a part of the real-world product
"""


class ColorTrend(models.Model):
    """
    Color Trend Model - Market Research Only
    """
    color_name = models.CharField(u'Name of Color', max_length=100)
    color_hex = models.CharField(u'Hex of the Color',
                                 max_length=7, primary_key=True)
    up_votes = models.PositiveIntegerField(null=True)
    down_votes = models.PositiveIntegerField(null=True)

    def __unicode__(self):
        return self.color_name


class DesignTrend(models.Model):
    """
    Design Trend Model - Market Research Only
    """
    design_ID = models.CharField(max_length=5, primary_key=True)
    design_name = models.CharField(u'Name of the Desgin', max_length=100)
    design_thumbnail = models.ImageField(u'Hero Photo', upload_to='designs')
    design_description = models.TextField(null=True)
    floor_cost = models.PositiveIntegerField()
    ceil_cost = models.PositiveIntegerField()

    def __unicode__(self):
        return self.design_name


class DesignTrendAvailableColors(models.Model):
    """
    Available colors to choose from for the designs
    """
    design_ID = models.ForeignKey('DesignTrend', related_name = "colors")
    design_colors = models.CharField(max_length=6, null=True)


class DesignTrendPhotos(models.Model):
    """
    Various photos to represent the designs
    """
    design_ID = models.ForeignKey('DesignTrend', related_name="photos")
    design_photos = models.ImageField(upload_to='designs')

    def __unicode__(self):
        return unicode(self.design_ID)


class UserIDTrend(models.Model):
    """
    User ID - Primary Key
    Voter IP - IP Address of the person visiting
    Voter Country - Two letter code of the country the person is visiting from
    User Sex - How do we get this?
    """

    user_id = models.CharField(primary_key=True, max_length=100)
    voter_ip = models.GenericIPAddressField(protocol='both', null=True)
    voter_country = models.CharField(max_length=40, null=True)

    def __unicode__(self):
        return self.user_id


class DesignSizesTrend(models.Model):
    """
    Design ID - Foreign Key to the DeisgnTrends model
    Sizes - Available Sizes
    """

    design_ID = models.ForeignKey('DesignTrend', related_name="sizes")
    sizes = models.CharField(max_length=4)

    def __unicode__(self):
        return unicode(self.design_ID)


class UserVotingTrend(models.Model):
    """
    User Voting Trend - Market Research Only

    Design ID - ForeignKey from DesignTrend model
    User ID - ForeignKey from UserIDTrend model
    howmuch - What is the user willing to pay for the product / design?
    NPS - How likely is it that the user will purchase this product / design?
    Preferred Size - Which Size of the product is the user likely to purchase?
    """

    design_ID = models.ForeignKey('DesignTrend')
    user_id = models.ForeignKey('UserIDTrend')
    how_much = models.PositiveIntegerField(null=True)
    nps = models.PositiveIntegerField(null=True)
    preferred_size = models.CharField(max_length=4, null=True)

    def __unicode__(self):
        return unicode(self.design_ID)

    class Meta:
        unique_together = ('design_ID', 'user_id', )


class Competition(models.Model):
    """
    Competition model

    name - competition name
    image - cover photo
    prizes - ist of all product prizes for competition
    """
    name = models.CharField(u'Name of Competition', max_length=200)
    image = models.ImageField(u'Photo of Competition', upload_to='competition')
    description = models.TextField(blank=True, null=True)

    prizes = models.ManyToManyField(
        'Prize', related_name='competitions', through='PrizeCompetitionRef')

    active_flag = models.BooleanField(default=True, verbose_name=u"Is Active")
    top_flag = models.BooleanField(
        default=False, verbose_name=u"Show on First page")

    # all users who participates in competition
    users = models.ManyToManyField(
        'MyUser', through='UserCompetitionRef')

    end_date = models.DateField(null=True)
    end_flag = models.BooleanField(default=False)

    @property
    def photos(self):
        return Photo.objects.filter(competition=self).filter(active_flag=True)

    @property
    def tagged_name(self):
        return "#" + self.name

    def __unicode__(self):
        return self.name

    @staticmethod
    def get_active():
        competition_list = Competition.objects.filter(
            top_flag=True, active_flag=True)
        if competition_list.count() != 0:
            return competition_list[0]
        else:
            raise Exception("Competition not found")


class Photo(models.Model):
    """
    User photo uploaded for Competition
    """
    ABUSE_TYPES = (
        ('content', 'PHOTO FROM ANOTHER SOURCE'),
        ('inappropriate', 'INAPPROPRIATE PHOTO'),
        ('notrelevant', 'NOT RELEVENT TO THE CONTEST'),
        ('spam', 'THIS IS A SPAM !'),
    )

    author = models.ForeignKey('MyUser', verbose_name=u"author")
    competition = models.ForeignKey(
        Competition, verbose_name=u"Competition", related_name="all_photos")

    create_date = models.DateTimeField(auto_now=True)

    image = models.ImageField(u'Photo', upload_to='photo')

    active_flag = models.BooleanField(default=True)
    spam_flag = models.BooleanField(default=False)
    abuse_reason = models.CharField(
        choices=ABUSE_TYPES, max_length=20, blank=True)

    @staticmethod
    def get_photo_name():
        return "{0}.jpg".format(''.join(random.choice(
            string.ascii_letters + string.digits) for _ in range(10)))

    class Meta:
        ordering = ['-create_date', ]


class Category(MP_Node):
    """
    Product Categories model
    """
    name = models.CharField(max_length=250L)
    view_flag = models.BooleanField(default=True)
    children = None

    node_order_by = ['name', ]

    def __unicode__(self):
        return self.name


class Prize(models.Model):
    """
    Product Prize model
    """
    SIZES = (
        ('One size', 'One size'),
        ('XXS', 'XXS'), ('XS', 'XS'), ('S', 'S'),
        ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'),
        ('2', '2'), ('4', '4'), ('6', '6'), ('8', '8'),
        ('10', '10'), ('12', '12'), ('14', '14'), ('16', '16'),
    )

    SIZE_TYPES = (
        ('US', 'US'), ('UK', 'UK'), ('EU', 'EU'), ('Asia', 'Asia'),
    )

    TEMPERATURE = (
        ('Hot', 'Hot'), ('Warm', 'Warm'), ('Mild', 'Mild'), ('Rain', 'Rain'),
        ('Cool', 'Cool'), ('Cold', 'Cold'), ('Freezing', 'Freezing'),
    )

    PRIZE_TYPES = (
        ('rv', 'Random vote'),
        ('bp', 'Best photo'),
    )

    RANDOM_VOTE = 'rv'
    BEST_PHOTO = 'bp'

    number = models.CharField(u'Product Number', max_length=100)
    name = models.CharField(u'Name of Product', max_length=100)
    retail_price = models.DecimalField(max_digits=9, decimal_places=2)
    discount_amount = models.IntegerField(
        blank=True,
        null=True,
        help_text="Discount in percent (%), only numbers, ie 15"
        )
    sale_price = models.IntegerField(blank=True)
    purchase_price = models.DecimalField(max_digits=9, decimal_places=2)

    thumbnail = models.ImageField(u'Thumbnail', upload_to='prize')
    hover_description = models.CharField(max_length=30, null=True, blank=True)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    temperature = models.CharField(
        choices=TEMPERATURE, max_length=20, null=True, blank=True)

    sizes = SelectMultipleField(choices=SIZES, max_length=100)
    size_type = models.CharField(choices=SIZE_TYPES, max_length=100)
    colors = models.ManyToManyField('ProductColor', related_name='products')
    measurement_chart = models.FileField(
        upload_to='measurement_chart', blank=True)
    description = models.TextField()

    delivery_time = models.CharField(max_length=250, null=True, blank=True)
    shipping_cost = models.CharField(max_length=250, null=True, blank=True)

    create_date = models.DateTimeField(
        auto_now_add=True, verbose_name=u'Added')
    website_link = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        ordering = ['name', ]

    def __unicode__(self):
        return self.name


class PrizeGroupRef(models.Model):
    """
    Many-to-Many relation for Group-prize
    with prize type (best photo, random vote)
    """
    group = models.ForeignKey('PrizeGroup')
    prize = models.ForeignKey('Prize')
    prize_type = models.CharField(choices=Prize.PRIZE_TYPES, max_length=2)


class PrizeGroup(models.Model):
    """
    Prize groups for competition winners
    """
    name = models.CharField(max_length=50)
    code = models.SlugField(max_length=20)
    prizes = models.ManyToManyField(
        'Prize', through=PrizeGroupRef, related_name='groups')

    def __unicode__(self):
        return self.name


class ProductPhoto(models.Model):
    """
    Photos for Prize Products
    """
    prize = models.ForeignKey(u'Prize', related_name="photos")
    image = models.ImageField(u'Photo', upload_to='product_photo')


class ProductColor(models.Model):
    """
    Prize Product colors
    """
    name = models.CharField(max_length=100)
    color_code = models.CharField(u'Color HTML Code', max_length=7)

    def __unicode__(self):
        return self.name


class UserCompetitionRef(models.Model):
    """
    Link between user and competition
    """
    user = models.ForeignKey('MyUser')
    competition = models.ForeignKey('Competition')
    vote_count = models.IntegerField(blank=True, default=0)


class VoteHistory(models.Model):
    """
    Every user vote  (for photo, or for share) logs here
    """

    VOTE_TYPES = (
        ('V', 'Vote'),
        ('S', 'Share'),
    )

    VOTE_TYPE = 'V'
    SHARE_TYPE = 'S'

    create_date = models.DateTimeField(auto_now=True)
    from_user = models.ForeignKey(
        'MyUser', related_name='votes_given')  # Who gives vote
    to_user = models.ForeignKey(
        'MyUser', related_name='votes_received')  # Who receives vote
    session = models.CharField(max_length=100, blank=True)
    competition = models.ForeignKey('Competition')
    photo = models.ForeignKey('Photo', related_name='vote_history')
    vote_count = models.IntegerField(default=1)
    vote_type = models.CharField(choices=VOTE_TYPES, max_length=1)


class ViewHistory(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    from_user = models.ForeignKey(
        'MyUser', related_name='viewed_photos')  # Who gives vote
    competition = models.ForeignKey('Competition')
    photo = models.ForeignKey('Photo', related_name='view_history')


class MyUserManager(BaseUserManager):
    """
    Create user functions

    """
    def create_user(self, email, password=None, **extra_fields):
        # if not email:
        # raise ValueError('Users must have a email')
        """
        :param email:
        :param password:
        :param extra_fields:
        :return:
        """
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model
    """
    objects = MyUserManager()

    # additional fields
    upload_path = 'user'
    avatar = models.ImageField(
        u'Profile image', upload_to=upload_path, blank=True)

    username = models.CharField(_('username'), max_length=30, unique=True,
                                help_text=_('Required. 30 characters or fewer.'
                                            'Letters, digits, @/./+/-/_ only'),
                                validators=[
            validators.RegexValidator(r'^[\s\w.@+-]+$',
                                      _('Enter a valid username. '
                                        'This value may contain only letters, numbers '
                                        'and @/./+/-/_ characters.'), 'invalid'),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        })
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(_(
        'staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    terms_flag = models.BooleanField(default=False, editable=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.username

    def get_absolute_url(self):
        return '/user/' + str(self.id) + '/'

    class Meta:
        app_label = 'main'


class PrizeCompetitionRef(models.Model):
    """
    Many-to-Many relation for Competition-prize
    with prize type (best photo, random vote)
    """
    competition = models.ForeignKey('Competition')
    prize = models.ForeignKey('Prize')
    prize_type = models.CharField(choices=Prize.PRIZE_TYPES, max_length=2)


class Winner(models.Model):
    """
    winners history for competitions
    """
    create_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('MyUser')
    competition = models.ForeignKey('Competition', related_name='winners')
    photo = models.ForeignKey('Photo', null=True)
    prize = models.ForeignKey('Prize', null=True)
    prize_group = models.ForeignKey('PrizeGroup',
                                    null=True, related_name="winners")
    prize_type = models.CharField(choices=Prize.PRIZE_TYPES, max_length=2)
    code = models.UUIDField(default=uuid.uuid4)

    def get_end_date(self):
        return self.create_date - datetime.datetime.delta(days=1)


class Config(models.Model):
    """
    Configuration
    """
    WEEK_DAYS = [
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        ('7', 'Sunday'),
    ]

    name = models.CharField(max_length=100, default='Website settings')
    refresh_week_day = models.CharField(
        choices=WEEK_DAYS, max_length=1, default='3')
    first_page_text = models.TextField(
        default='<h2 id="numero6"><a href="" ng-click="selectPhotoFromDesktop()">Enter a photo</a> or <a href="">vote</a></h2>' +
            '<h4>in photo competitions to win one of these prizes:</h4>')