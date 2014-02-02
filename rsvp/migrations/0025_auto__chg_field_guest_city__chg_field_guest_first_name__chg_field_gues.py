# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Guest.city'
        db.alter_column(u'rsvp_guest', 'city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Guest.first_name'
        db.alter_column(u'rsvp_guest', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=45, null=True))

        # Changing field 'Guest.last_name'
        db.alter_column(u'rsvp_guest', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=45, null=True))

        # Changing field 'Guest.street_addr'
        db.alter_column(u'rsvp_guest', 'street_addr', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Guest.primary'
        db.alter_column(u'rsvp_guest', 'primary', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'Guest.attending'
        db.alter_column(u'rsvp_guest', 'attending', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'Guest.state'
        db.alter_column(u'rsvp_guest', 'state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'Guest.primary_email'
        db.alter_column(u'rsvp_guest', 'primary_email', self.gf('django.db.models.fields.EmailField')(max_length=254, null=True))

        # Changing field 'Guest.zip_code'
        db.alter_column(u'rsvp_guest', 'zip_code', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True))

    def backwards(self, orm):

        # Changing field 'Guest.city'
        db.alter_column(u'rsvp_guest', 'city', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'Guest.first_name'
        db.alter_column(u'rsvp_guest', 'first_name', self.gf('django.db.models.fields.CharField')(default='', max_length=45))

        # Changing field 'Guest.last_name'
        db.alter_column(u'rsvp_guest', 'last_name', self.gf('django.db.models.fields.CharField')(default='', max_length=45))

        # Changing field 'Guest.street_addr'
        db.alter_column(u'rsvp_guest', 'street_addr', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'Guest.primary'
        db.alter_column(u'rsvp_guest', 'primary', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Guest.attending'
        db.alter_column(u'rsvp_guest', 'attending', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Guest.state'
        db.alter_column(u'rsvp_guest', 'state', self.gf('django.db.models.fields.CharField')(default='', max_length=2))

        # Changing field 'Guest.primary_email'
        db.alter_column(u'rsvp_guest', 'primary_email', self.gf('django.db.models.fields.EmailField')(default='', max_length=254))

        # Changing field 'Guest.zip_code'
        db.alter_column(u'rsvp_guest', 'zip_code', self.gf('django.db.models.fields.IntegerField')(default='', max_length=5))

    models = {
        u'rsvp.event': {
            'Meta': {'object_name': 'Event'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsvp.Location']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rsvp.guest': {
            'Meta': {'ordering': "['-last_name', '-first_name']", 'object_name': 'Guest'},
            'attending': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'events': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['rsvp.Event']", 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsvp.Hotel']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'primary': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'primary_email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'street_addr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        u'rsvp.hotel': {
            'Meta': {'object_name': 'Hotel'},
            'hotel_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'total_guest_count': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'})
        },
        u'rsvp.location': {
            'Meta': {'object_name': 'Location'},
            'distance': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rsvp.party': {
            'Meta': {'object_name': 'Party'},
            'guests': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['rsvp.Guest']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_size': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rsvp.room': {
            'Meta': {'object_name': 'Room'},
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsvp.Hotel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_occupancy': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'room_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsvp.Roomtype']", 'null': 'True', 'blank': 'True'})
        },
        u'rsvp.roomtype': {
            'Meta': {'object_name': 'Roomtype'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rsvp.table': {
            'Meta': {'object_name': 'Table'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['rsvp']