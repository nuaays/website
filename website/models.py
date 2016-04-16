from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, UserManager
from datetime import datetime
from time import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(_('username'), max_length=128, unique=True)
    # this column is called first_name for legacy reasons, but it is the entire
    # display name
    name = models.CharField(_('name'), max_length=200, blank=True,
                            db_column='first_name')
    org_name = models.CharField(_('organization name'), max_length=200, blank=True, null=True)
    phone = models.CharField(_('phone number'), max_length=20, blank=True, null=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(
        _('active'), default=False,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    is_superuser = models.BooleanField(
        _('superuser status'), default=False,
        help_text=_('Designates that this user has all permissions without '
                    'explicitly assigning them.'))
    is_managed = models.BooleanField(
        _('managed'), default=False,
        help_text=_('Designates whether this user should be treated as '
                    'managed. Select this to disallow the user from '
                    'modifying their account (username, password, etc).'))

    date_joined = models.DateTimeField(_('date joined'), default=datetime.now())

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        app_label = 'website'
        db_table = 'auth_user'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def delete(self):
        if self.username == 'sentry':
            raise Exception('You cannot delete the "sentry" user as it is required by Sentry.')
        return super(User, self).delete()

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        return super(User, self).save(*args, **kwargs)

    def get_display_name(self):
        return self.name or self.email or self.username

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

def datetime_now():
    return datetime.datetime.now()


class Organization(models.Model):
    organization_name = models.CharField(max_length=128, unique=True)
    domain_name = models.CharField(max_length=256, unique=True)
    sentry_instance = models.CharField(max_length=256)


class UserDetail(models.Model):
    email = models.EmailField(max_length=256, )
    password = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True)
    name = models.CharField(max_length=256, null=True)
    company = models.CharField(max_length=256, null=True)
    server_count = models.IntegerField(null=True)
    user = models.ForeignKey(User)
    org_name = models.CharField(max_length=128, null=True)
    domain_name = models.CharField(max_length=128, null=True)

    def send_activation_email(self, site):
        pass


class SentryInstance(models.Model):
    sentry_instance_name = models.CharField(max_length=128, unique=True)
    sentry_instance_url_prefix = models.CharField(max_length=250)
    client_id = models.CharField(max_length=512, null=True)
    client_secret = models.CharField(max_length=512, null=True)
