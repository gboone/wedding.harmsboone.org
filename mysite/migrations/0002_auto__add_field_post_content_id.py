# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.content_id'
        db.add_column(u'mysite_post', 'content_id',
                      self.gf('django.db.models.fields.CharField')(default='waters', max_length=64),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.content_id'
        db.delete_column(u'mysite_post', 'content_id')


    models = {
        u'mysite.post': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Post'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['mysite']