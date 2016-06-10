"""
Form components for working with trees.
"""
from __future__ import unicode_literals
from django import forms
from django.forms.forms import NON_FIELD_ERRORS
try:
    from django.utils.encoding import smart_text
except ImportError:  # pragma: no cover (Django 1.4 compatibility)
    from django.utils.encoding import smart_unicode as smart_text
from django.utils.html import conditional_escape, mark_safe
from django.utils.translation import ugettext_lazy as _

__all__ = (
    'TreeNodeChoiceField',
)

# Fields ######################################################################


class TreeNodeChoiceFieldMixin(object):
    def __init__(self, queryset, *args, **kwargs):
        self.level_indicator = kwargs.pop('level_indicator', ".....")
        super(TreeNodeChoiceFieldMixin, self).__init__(queryset, *args, **kwargs)

    def _get_level_indicator(self, obj):
        level = obj.get_depth()
        return mark_safe(conditional_escape(self.level_indicator) * (level - 1))

    def label_from_instance(self, obj):
        """
        Creates labels which represent the tree level of each node when
        generating option labels.
        """
        level_indicator = self._get_level_indicator(obj)
        return mark_safe(level_indicator + ' ' + conditional_escape(smart_text(obj)))


class TreeNodeChoiceField(TreeNodeChoiceFieldMixin, forms.ModelChoiceField):
    """A ModelChoiceField for tree nodes."""



