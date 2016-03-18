"""
sentry.models.organizationmember
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2010-2014 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
from __future__ import absolute_import, print_function

import logging

from bitfield import BitField
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models, transaction
from django.db.models import F
from django.utils import timezone
from hashlib import md5
from website import roles
from website.models.foreignkey import FlexibleForeignKey
from website.models.bounded import BoundedPositiveIntegerField


class OrganizationMember(models.Model):
    """
    Identifies relationships between teams and users.

    Users listed as team members are considered to have access to all projects
    and could be thought of as team owners (though their access level may not)
    be set to ownership.
    """
    organization = FlexibleForeignKey('sentry.Organization', related_name="member_set")

    user = FlexibleForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,
                             related_name="sentry_orgmember_set")
    email = models.EmailField(null=True, blank=True)
    role = models.CharField(
        choices=roles.get_choices(),
        max_length=32,
        default=roles.get_default().id,
    )
    flags = BitField(flags=(
        ('sso:linked', 'sso:linked'),
        ('sso:invalid', 'sso:invalid'),
    ), default=0)
    date_added = models.DateTimeField(default=timezone.now)
    has_global_access = models.BooleanField(default=True)
    counter = BoundedPositiveIntegerField(null=True, blank=True)
    teams = models.ManyToManyField('sentry.Team', blank=True,
                                   through='sentry.OrganizationMemberTeam')

    # Deprecated -- no longer used
    type = BoundedPositiveIntegerField(default=50, blank=True)

    class Meta:
        app_label = 'sentry'
        db_table = 'sentry_organizationmember'
        unique_together = (
            ('organization', 'user'),
            ('organization', 'email'),
        )


    @transaction.atomic
    def save(self, *args, **kwargs):
        assert self.user_id or self.email, \
            'Must set user or email'
        super(OrganizationMember, self).save(*args, **kwargs)

        if not self.counter:
            self._set_counter()

    @transaction.atomic
    def delete(self, *args, **kwargs):
        super(OrganizationMember, self).delete(*args, **kwargs)
        if self.counter:
            self._unshift_counter()

    def _unshift_counter(self):
        assert self.counter
        OrganizationMember.objects.filter(
            organization=self.organization,
            counter__gt=self.counter,
        ).update(
            counter=F('counter') - 1,
        )

    def _set_counter(self):
        assert self.id and not self.counter
        # XXX(dcramer): this isnt atomic, but unfortunately MySQL doesnt support
        # the subquery pattern we'd need
        self.update(
            counter=OrganizationMember.objects.filter(
                organization=self.organization,
            ).count(),
        )

    @property
    def is_pending(self):
        return self.user_id is None

    @property
    def token(self):
        checksum = md5()
        for x in (str(self.organization_id), self.get_email(), settings.SECRET_KEY):
            checksum.update(x)
        return checksum.hexdigest()

    def get_display_name(self):
        if self.user_id:
            return self.user.get_display_name()
        return self.email

    def get_email(self):
        if self.user_id:
            return self.user.email
        return self.email
