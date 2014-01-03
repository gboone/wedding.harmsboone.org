# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field guests on 'Event'
        m2m_table_name = db.shorten_name(u'rsvp_event_guests')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'rsvp.event'], null=False)),
            ('guest', models.ForeignKey(orm[u'rsvp.guest'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'guest_id'])

        # Removing M2M table for field room on 'Guest'
        db.delete_table(db.shorten_name(u'rsvp_guest_room'))

        # Removing M2M table for field hotel on 'Guest'
        db.delete_table(db.shorten_name(u'rsvp_guest_hotel'))

        # Removing M2M table for field table on 'Guest'
        db.delete_table(db.shorten_name(u'rsvp_guest_table'))

        # Removing M2M table for field event on 'Guest'
        db.delete_table(db.shorten_name(u'rsvp_guest_event'))

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


    def backwards(self, orm):
        # Removing M2M table for field guests on 'Event'
        db.delete_table(db.shorten_name(u'rsvp_event_guests'))

        # Adding M2M table for field room on 'Guest'
        m2m_table_name = db.shorten_name(u'rsvp_guest_room')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('guest', models.ForeignKey(orm[u'rsvp.guest'], null=False)),
            ('room', models.ForeignKey(orm[u'rsvp.room'], null=False))
        ))
        db.create_unique(m2m_table_name, ['guest_id', 'room_id'])

        # Adding M2M table for field hotel on 'Guest'
        m2m_table_name = db.shorten_name(u'rsvp_guest_hotel')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('guest', models.ForeignKey(orm[u'rsvp.guest'], null=False)),
            ('hotel', models.ForeignKey(orm[u'rsvp.hotel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['guest_id', 'hotel_id'])

        # Adding M2M table for field table on 'Guest'
        m2m_table_name = db.shorten_name(u'rsvp_guest_table')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('guest', models.ForeignKey(orm[u'rsvp.guest'], null=False)),
            ('table', models.ForeignKey(orm[u'rsvp.table'], null=False))
        ))
        db.create_unique(m2m_table_name, ['guest_id', 'table_id'])

        # Adding M2M table for field event on 'Guest'
        m2m_table_name = db.shorten_name(u'rsvp_guest_event')
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


    models = {
        u'rsvp.event': {
            'Meta': {'object_name': 'Event'},
            'guests': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['rsvp.Guest']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsvp.Location']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rsvp.guest': {
            'Meta': {'ordering': "['-last_name', '-first_name']", 'object_name': 'Guest'},
            'attending': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'display_as': ('django.db.models.fields.CharField', [], {'max_length': '91', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'max_guests': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
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
            'guests': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['rsvp.Guest']", 'null': 'True', 'blank': 'True'}),
            'hotel_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total_guest_count': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'})
        },
        u'rsvp.location': {
            'Meta': {'object_name': 'Location'},
            'distance': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rsvp.room': {
            'Meta': {'object_name': 'Room'},
            'guests': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['rsvp.Guest']", 'null': 'True', 'blank': 'True'}),
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsvp.Hotel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_occupancy': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'room_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'rsvp.table': {
            'Meta': {'object_name': 'Table'},
            'guests': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['rsvp.Guest']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['rsvp']