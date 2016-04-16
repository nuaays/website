# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'auth_user', (
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, db_column=u'first_name', blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_managed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 4, 15, 0, 0))),
        ))
        db.send_create_signal(u'website', ['User'])


        # Changing field 'UserDetail.user'
        db.alter_column(u'website_userdetail', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.User']))

    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'auth_user')


        # Changing field 'UserDetail.user'
        db.alter_column(u'website_userdetail', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

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
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_managed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "u'first_name'", 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
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