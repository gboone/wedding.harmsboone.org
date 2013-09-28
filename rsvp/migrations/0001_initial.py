# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Guest'
        db.create_table(u'rsvp_guest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('prefix', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('max_guests', self.gf('django.db.models.fields.IntegerField')()),
            ('attending', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('street_addr', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('zip_code', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
        ))
        db.send_create_signal(u'rsvp', ['Guest'])

        # Adding model 'Table'
        db.create_table(u'rsvp_table', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('guest_count', self.gf('django.db.models.fields.IntegerField')()),
            ('theme', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal(u'rsvp', ['Table'])

        # Adding model 'Events'
        db.create_table(u'rsvp_events', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'rsvp', ['Events'])


    def backwards(self, orm):
        # Deleting model 'Guest'
        db.delete_table(u'rsvp_guest')

        # Deleting model 'Table'
        db.delete_table(u'rsvp_table')

        # Deleting model 'Events'
        db.delete_table(u'rsvp_events')


    models = {
        u'rsvp.events': {
            'Meta': {'object_name': 'Events'},
            'event_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'rsvp.guest': {
            'Meta': {'ordering': "['-last_name', '-first_name']", 'object_name': 'Guest'},
            'attending': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'max_guests': ('django.db.models.fields.IntegerField', [], {}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'primary_email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'street_addr': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'max_length': '5'})
        },
        u'rsvp.table': {
            'Meta': {'object_name': 'Table'},
            'guest_count': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'theme': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        }
    }

    complete_apps = ['rsvp']