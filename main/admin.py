"""
Admin settings
"""
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.urlresolvers import reverse
from django.forms import BaseInlineFormSet
from django.http import HttpResponseRedirect
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from main.form import TreeNodeChoiceField
from main.models import Competition, Photo, MyUser, Prize
from main.models import ProductPhoto, ProductColor, VoteHistory, Category
from main.models import PrizeCompetitionRef, PrizeGroupRef
from main.models import PrizeGroup, Config, Winner
from main.models import ColorTrend, DesignTrend, DesignSizesTrend, DesignTrendPhotos, DesignTrendAvailableColors
from main.models import UserVotingTrend, UserIDTrend


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('username', 'email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = [
            'username', 'email', 'first_name', 'last_name',
            'password', 'avatar', 'is_active', 'is_staff',
            'is_superuser', 'groups'
            ]

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class MyUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = (
        'id', 'username', 'email', 'is_active', 'is_staff', 'is_superuser'
        )
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'first_name', 'last_name', 'password', 'avatar', 'terms_flag')}),
        (u'Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
        ),
    )
    search_fields = ('username', 'email', 'id')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)


class PrizeCompetitionInline(admin.TabularInline):
    model = PrizeCompetitionRef
    extra = 2


class CompetitionAdmin(admin.ModelAdmin):
    """
    Settings for Competition Admin Section
    """
    list_display = ['name', 'active_flag', 'top_flag', 'id', 'admin_thumbnail', 'end_date', ]
    inlines = [PrizeCompetitionInline,]

    def admin_thumbnail(self, obj):
        return u'<img src="%s" width="50"/>' % (obj.image.url)
    admin_thumbnail.short_description = 'Photo'
    admin_thumbnail.allow_tags = True

    def has_delete_permission(self, request, obj=None):
        return False


class PhotoAdmin(admin.ModelAdmin):
    """
    Settings for Photo Admin Section
    """
    def admin_thumbnail(self, obj):
        return u'<img src="%s" width="100"/>' % (obj.image.url)
    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True

    list_display = ['create_date', 'admin_thumbnail', 'id', 'active_flag', 'spam_flag', 'competition',  ]
    list_filter = ('active_flag', 'spam_flag', 'abuse_reason', )
    ordering = ('-create_date',)
    readonly_fields = ('admin_thumbnail',)

    def response_add(self, request, obj, post_url_continue=None):
        if request.POST.has_key('_addanother'):
            url = reverse("admin:main_photo_add")
            competition_id = request.POST['competition']
            author_id = request.POST['author']
            qs = '?competition=%s&author=%s' % (competition_id, author_id)
            return HttpResponseRedirect(''.join((url, qs)))
        else:
            return HttpResponseRedirect(reverse("admin:main_photo_changelist"))

    def response_change(self, request, obj, post_url_continue=None):
        if request.POST.has_key('_addanother'):
            url = reverse("admin:main_photo_add")
            competition_id = request.POST['competition']
            author_id = request.POST['author']
            qs = '?competition=%s&author=%s' % (competition_id, author_id)
            return HttpResponseRedirect(''.join((url, qs)))
        else:
            return HttpResponseRedirect(reverse("admin:main_photo_changelist"))


class PrizeAdminForm(forms.ModelForm):
    """
    Form for Prize in admin
    """
    sizes = forms.MultipleChoiceField(choices=Prize.SIZES, widget=forms.CheckboxSelectMultiple())
    #colors = forms.ModelMultipleChoiceField(queryset=ProductColor.objects.all(), widget=forms.CheckboxSelectMultiple())
    category = TreeNodeChoiceField(queryset=Category.objects.all(), required=False)

    def clean(self):
        #checking if sale > purchase price
        cleaned_data = self.cleaned_data
        if cleaned_data.get("purchase_price") > cleaned_data.get("sale_price"):
            self._errors["sale_price"] = self.error_class([u"Sale Price less then Purchase Price"])
        return cleaned_data


class AtLeastOneRequiredInlineFormSet(BaseInlineFormSet):

    def clean(self):
        """Check that at least one photo has been entered."""
        super(AtLeastOneRequiredInlineFormSet, self).clean()
        if any(self.errors):
            return
        if not any(cleaned_data and not cleaned_data.get('DELETE', False)
                    for cleaned_data in self.cleaned_data):
            raise forms.ValidationError('At least one item required.')


class ProductPhotoInline(admin.TabularInline):
    """
    Inline for Product photos
    """
    model = ProductPhoto
    formset = AtLeastOneRequiredInlineFormSet
    extra = 5

    def admin_thumbnail(self, obj):
        return u'<img src="%s" width="100"/>' % (obj.image.url)
    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True
    readonly_fields = ['admin_thumbnail', ]


class SelectWidgetFilter(admin.RelatedOnlyFieldListFilter):
    template = "admin_filter.html"


class PrizeAdmin(admin.ModelAdmin):
    """
    Settings for Prize Product Admin Section
    """
    def admin_thumbnail(self, obj):
        return u'<img src="%s" width="100"/>' % (obj.thumbnail.url)
    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True

    list_display = ['name', 'admin_thumbnail', 'create_date', 'number', 'id', 'retail_price', 'sale_price', ]
    list_filter = [
        ('category', SelectWidgetFilter), 'temperature', ('colors', SelectWidgetFilter), ]
    form = PrizeAdminForm
    inlines = [ProductPhotoInline,]
    readonly_fields = ['admin_thumbnail', 'create_date']

    filter_horizontal = ('colors',)

    class Media:
        js = (
            'js/admin.js',
        )


class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)


class ProductColorAdmin(admin.ModelAdmin):
    """
    Settings for Product Colors Admin Section
    """
    list_display = ['name', 'id', ]


class VoteHistoryAdmin(admin.ModelAdmin):
    """
    Settings for Vote History Admin Section
    """
    list_display = ['id', 'create_date', 'competition', 'photo', 'vote_count',
                    ]


class PrizeGroupInline(admin.TabularInline):
    model = PrizeGroupRef
    extra = 2


class PrizeGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'id', ]
    inlines = [PrizeGroupInline, ]


class ConfigAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', ]


class WinnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'create_date', 'code', ]


class ColorTrendAdmin(admin.ModelAdmin):

    def colorbox(self, obj):
        return u'<div style="display: block; background-color: #%s; width: 50px; height: 50px;"></div>' % (obj.color_hex)
    colorbox.short_description = 'Color'
    colorbox.allow_tags = True
    list_display = ['colorbox', 'color_name', 'color_hex', 'up_votes', ]


class DesignSizesTrendAdmin(admin.TabularInline):
    model = DesignSizesTrend
    list_display = ['design_ID', 'sizes', ]


class DesignTrendPhotosAdmin(admin.TabularInline):
    model = DesignTrendPhotos
    list_display = ['design_ID', 'design_photos', ]


class UserVotingTrendAdmin(admin.TabularInline):
    model = UserVotingTrend
    readonly_fields = ['design_ID', 'user_id', 'how_much',
                    'nps', 'preferred_size',
                    ]               

class DesignTrendAvailableColorsAdmin(admin.TabularInline):
    model = DesignTrendAvailableColors
    list_display = ['design_ID', 'design_colors']


class UserIDTrendAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'voter_ip', 'voter_country', ]


class DesignTrendAdmin(admin.ModelAdmin):

    def designtrend_thumbnail(self, obj):
        return u'<img src="/media/%s" width="100"/>' % (obj.design_thumbnail)
    designtrend_thumbnail.short_description = 'Thumbnail'
    designtrend_thumbnail.allow_tags = True

    list_display = ['design_ID', 'design_name',
                    'design_description', 'designtrend_thumbnail',
                    ]

    inlines = [DesignTrendAvailableColorsAdmin, DesignSizesTrendAdmin,
               DesignTrendPhotosAdmin,
               UserVotingTrendAdmin]


admin.site.site_header = 'FOMO Backend'

admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(PrizeGroup, PrizeGroupAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Prize, PrizeAdmin)
admin.site.register(ProductColor, ProductColorAdmin)
admin.site.register(VoteHistory, VoteHistoryAdmin)
admin.site.register(Config, ConfigAdmin)
admin.site.register(Winner, WinnerAdmin)
admin.site.register(ColorTrend, ColorTrendAdmin)
admin.site.register(DesignTrend, DesignTrendAdmin)
admin.site.register(UserIDTrend, UserIDTrendAdmin)
