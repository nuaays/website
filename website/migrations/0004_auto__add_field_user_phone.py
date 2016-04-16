# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.phone'
        db.add_column(u'auth_user', 'phone',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'User.phone'
        db.delete_column(u'auth_user', 'phone')


    models = {
        u'website.organization': {
            'Meta': {'object_name': 'Organization'},
            'domain_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'sentry_instance': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'website.sentryinstance': {
            'Meta': {'object_name': 'SentryInstance'},
            'client_id': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'client_secret': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sentry_instance_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'sentry_instance_url_prefix': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'website.user': {
            'Meta': {'object_name': 'User', 'db_table': "u'auth_user'"},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 4, 15, 0, 0)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_managed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "u'first_name'", 'blank': 'True'}),
            'org_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'website.userdetail': {
            'Meta': {'object_name': 'UserDetail'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'domain_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'org_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True'}),
            'server_count': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['website.User']"})
        }
    }

    complete_apps = ['website']