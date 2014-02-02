# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field guests on 'Event'
        db.delete_table(db.shorten_name(u'rsvp_event_guests'))

        # Adding field 'Guest.hotel'
        db.add_column(u'rsvp_guest', 'hotel',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rsvp.Hotel'], null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field events on 'Guest'
        m2m_table_name = db.shorten_name(u'rsvp_guest_events')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('guest', models.ForeignKey(orm[u'rsvp.guest'], null=False)),
            ('event', models.ForeignKey(orm[u'rsvp.event'], null=False))
        ))
        db.create_unique(m2m_table_name, ['guest_id', 'event_id'])

        # Removing M2M table for field guests on 'Table'
        db.delete_table(db.shorten_name(u'rsvp_table_guests'))

        # Removing M2M table for field guests on 'Hotel'
        db.delete_table(db.shorten_name(u'rsvp_hotel_guests'))

        # Removing M2M table for field guests on 'Room'
        db.delete_table(db.shorten_name(u'rsvp_room_guests'))


    def backwards(self, orm):
        # Adding M2M table for field guests on 'Event'
        m2m_table_name = db.shorten_name(u'rsvp_event_guests')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'rsvp.event'], null=False)),
            ('guest', models.ForeignKey(orm[u'rsvp.guest'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'guest_id'])

        # Deleting field 'Guest.hotel'
        db.delete_column(u'rsvp_guest', 'hotel_id')

        # Removing M2M table for field events on 'Guest'
        db.delete_table(db.shorten_name(u'rsvp_guest_events'))

        # Adding M2M table for field guests on 'Table'
        m2m_table_name = db.shorten_name(u'rsvp_table_guests')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('table', models.ForeignKey(orm[u'rsvp.table'], null=False)),
            ('guest', models.ForeignKey(orm[u'rsvp.guest'], null=False))
        ))
        db.create_unique(m2m_table_name, ['table_id', 'guest_id'])

        # Adding M2M table for field guests on 'Hotel'
        m2m_table_name = db.shorten_name(u'rsvp_hotel_guests')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hotel', models.ForeignKey(orm[u'rsvp.hotel'], null=False)),
            ('guest', models.ForeignKey(orm[u'rsvp.guest'], null=False))
        ))
        db.create_unique(m2m_table_name, ['hotel_id', 'guest_id'])

        # Adding M2M table for field guests on 'Room'
        m2m_table_name = db.shorten_name(u'rsvp_room_guests')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('room', models.ForeignKey(orm[u'rsvp.room'], null=False)),
            ('guest', models.ForeignKey(orm[u'rsvp.guest'], null=False))
        ))
        db.create_unique(m2m_table_name, ['room_id', 'guest_id'])


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
            'max_guests': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'nights': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "'None'", 'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsvp.Guest']", 'null': 'True', 'blank': 'True'}),
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
            'distance': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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