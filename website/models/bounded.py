"""
sentry.db.models.fields.bounded
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2010-2014 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from __future__ import absolute_import

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from south.modelsinspector import add_introspection_rules

__all__ = (
    'BoundedAutoField', 'BoundedBigAutoField', 'BoundedIntegerField',
    'BoundedBigIntegerField', 'BoundedPositiveIntegerField'
)


class BoundedIntegerField(models.IntegerField):
    MAX_VALUE = 2147483647

    def get_prep_value(self, value):
        if value:
            value = int(value)
            assert value <= self.MAX_VALUE
        return super(BoundedIntegerField, self).get_prep_value(value)


class BoundedPositiveIntegerField(models.PositiveIntegerField):
    MAX_VALUE = 2147483647

    def get_prep_value(self, value):
        if value:
            value = int(value)
            assert value <= self.MAX_VALUE
        return super(BoundedPositiveIntegerField, self).get_prep_value(value)


class BoundedAutoField(models.AutoField):
    MAX_VALUE = 2147483647

    def get_prep_value(self, value):
        if value:
            value = int(value)
            assert value <= self.MAX_VALUE
        return super(BoundedAutoField, self).get_prep_value(value)



add_introspection_rules([], ["^sentry\.db\.models\.fields\.bounded\.BoundedAutoField"])
add_introspection_rules([], ["^sentry\.db\.models\.fields\.bounded\.BoundedBigAutoField"])
add_introspection_rules([], ["^sentry\.db\.models\.fields\.bounded\.BoundedIntegerField"])
add_introspection_rules([], ["^sentry\.db\.models\.fields\.bounded\.BoundedBigIntegerField"])
add_introspection_rules([], ["^sentry\.db\.models\.fields\.bounded\.BoundedPositiveIntegerField"])
add_introspection_rules([], ["^sentry\.db\.models\.fields\.pickle\.UnicodePickledObjectField"])
