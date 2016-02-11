from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import datetime


# Create your models here.

def datetime_now():
    return datetime.datetime.now()

 class UserDetail(models.Model):
  email = models.EmailField(max_length=256, )
  password = models.CharField(max_length=128, null=True, blank=True)
  phone = models.CharField(max_length=12, null=True)
  name = models.CharField(max_length=256, null=True)
  company = models.CharField(max_length=256, null=True)
  server_count = models.IntegerField(null=True)
  user = models.ForeignKey(User)

  def send_activation_email(self, site):
    ctx_dict = {'activation_key': self.activation_key,
                'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS,
                'site': site}
    subject = render_to_string('accounts/activation_email_subject.txt',
                                ctx_dict)
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())
                                       
    message = render_to_string('accounts/activation_email.txt',
                                ctx_dict)
                                                        
    self.user.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)


 def activation_key_expired(self):
    expiration_date = datetime.timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS)
    return self.activation_key == u"ALREADY_ACTIVATED" or \
          (self.user.date_joined + expiration_date <= datetime_now())
