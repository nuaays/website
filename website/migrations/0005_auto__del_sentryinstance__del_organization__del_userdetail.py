# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'SentryInstance'
        db.delete_table(u'website_sentryinstance')

        # Deleting model 'Organization'
        db.delete_table(u'website_organization')

        # Deleting model 'UserDetail'
        db.delete_table(u'website_userdetail')


    def backwards(self, orm):
        # Adding model 'SentryInstance'
        db.create_table(u'website_sentryinstance', (
            ('sentry_instance_url_prefix', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('sentry_instance_name', self.gf('django.db.models.fields.CharField')(max_length=128, unique=True)),
            ('client_id', self.gf('django.db.models.fields.CharField')(max_length=512, null=True)),
            ('client_secret', self.gf('django.db.models.fields.CharField')(max_length=512, null=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'website', ['SentryInstance'])

        # Adding model 'Organization'
        db.create_table(u'website_organization', (
            ('organization_name', self.gf('django.db.models.fields.CharField')(max_length=128, unique=True)),
            ('domain_name', self.gf('django.db.models.fields.CharField')(max_length=256, unique=True)),
            ('sentry_instance', self.gf('django.db.models.fields.CharField')(max_length=256)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'website', ['Organization'])

        # Adding model 'UserDetail'
        db.create_table(u'website_userdetail', (
            ('org_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=12, null=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('domain_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True)),
            ('server_count', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=256)),
        ))
        db.send_create_signal(u'website', ['UserDetail'])


    models = {
        
    }

    complete_apps = ['website']