"""
sentry.models.organization
~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2010-2014 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
from __future__ import absolute_import, print_function

from bitfield import BitField
from django.conf import settings
from django.db import IntegrityError, models, transaction
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from website.models.bounded import BoundedPositiveIntegerField
from website import roles


# TODO(dcramer): pull in enum library
class OrganizationStatus(object):
    VISIBLE = 0
    PENDING_DELETION = 1
    DELETION_IN_PROGRESS = 2


class Organization(models.Model):
    """
    An organization represents a group of individuals which maintain ownership of projects.
    """
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    status = BoundedPositiveIntegerField(choices=(
        (OrganizationStatus.VISIBLE, _('Visible')),
        (OrganizationStatus.PENDING_DELETION, _('Pending Deletion')),
        (OrganizationStatus.DELETION_IN_PROGRESS, _('Deletion in Progress')),
    ), default=OrganizationStatus.VISIBLE)
    date_added = models.DateTimeField(default=timezone.now)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='sentry.OrganizationMember', related_name='org_memberships')
    default_role = models.CharField(
        choices=roles.get_choices(),
        max_length=32,
        default=roles.get_default().id,
    )

    flags = BitField(flags=(
        ('allow_joinleave', 'Allow members to join and leave teams without requiring approval.'),
        ('enhanced_privacy', 'Enable enhanced privacy controls to limit personally identifiable information (PII) as well as source code in things like notifications.'),
        ('disable_shared_issues', 'Disable sharing of limited details on issues to anonymous users.'),
    ), default=1)


    class Meta:
        app_label = 'sentry'
        db_table = 'sentry_organization'


    @classmethod
    def get_default(cls):
        """
        Return the organization used in single organization mode.
        """
        return cls.objects.filter(
            status=OrganizationStatus.VISIBLE,
        )[0]

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.slug)

    def save(self, *args, **kwargs):
        if not self.slug:
            # lock_key = 'slug:organization'
            # with Lock(lock_key):
            #     slugify_instance(self, self.name,
            #                      reserved=RESERVED_ORGANIZATION_SLUGS)
            super(Organization, self).save(*args, **kwargs)
        else:
            super(Organization, self).save(*args, **kwargs)

    def delete(self):
        if self.is_default:
            raise Exception('You cannot delete the the default organization.')
        return super(Organization, self).delete()

    @cached_property
    def is_default(self):
        if not settings.SENTRY_SINGLE_ORGANIZATION:
            return False

        return self == type(self).get_default()

    def has_access(self, user, access=None):
        queryset = self.member_set.filter(user=user)
        if access is not None:
            queryset = queryset.filter(type__lte=access)

        return queryset.exists()

    def get_audit_log_data(self):
        return {
            'id': self.id,
            'slug': self.slug,
            'name': self.name,
            'status': self.status,
            'flags': self.flags,
            'default_role': self.default_role,
        }

    def get_default_owner(self):
        if not hasattr(self, '_default_owner'):
            from sentry.models import User

            self._default_owner = User.objects.filter(
                sentry_orgmember_set__role=roles.get_top_dog().id,
                sentry_orgmember_set__organization=self,
            )[0]
        return self._default_owner

