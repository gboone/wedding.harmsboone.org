# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Location.distance'
        db.alter_column(u'rsvp_location', 'distance', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=1))

    def backwards(self, orm):

        # Changing field 'Location.distance'
        db.alter_column(u'rsvp_location', 'distance', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2))

    models = {
        u'rsvp.event': {
            'Meta': {'object_name': 'Event'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsvp.Location']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rsvp.guest': {
            'Meta': {'ordering': "['-last_name', '-first_name']", 'object_name': 'Guest'},
            'arriving': ('django.db.models.fields.DateField', [], {'default': "'2014-08-14'"}),
            'attending': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'departing': ('django.db.models.fields.DateField', [], {'default': "'2014-08-17'"}),
            'display_as': ('django.db.models.fields.CharField', [], {'max_length': '91', 'null': 'True'}),
            'events': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['rsvp.Event']", 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsvp.Hotel']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'nights': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "'None'", 'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'street_addr': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'max_length': '5'})
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
            'max_size': ('django.db.models.fields.IntegerField', [], {'default': '1'})
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