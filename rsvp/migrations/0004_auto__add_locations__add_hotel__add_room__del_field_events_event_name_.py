# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Locations'
        db.create_table(u'rsvp_locations', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('distance', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'rsvp', ['Locations'])

        # Adding model 'Hotel'
        db.create_table(u'rsvp_hotel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'rsvp', ['Hotel'])

        # Adding M2M table for field guests on 'Hotel'
        m2m_table_name = db.shorten_name(u'rsvp_hotel_guests')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hotel', models.ForeignKey(orm[u'rsvp.hotel'], null=False)),
            ('guest', models.ForeignKey(orm[u'rsvp.guest'], null=False))
        ))
        db.create_unique(m2m_table_name, ['hotel_id', 'guest_id'])

        # Adding model 'Room'
        db.create_table(u'rsvp_room', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('hotel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rsvp.Hotel'])),
            ('max_occupancy', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'rsvp', ['Room'])

        # Adding M2M table for field guests on 'Room'
        m2m_table_name = db.shorten_name(u'rsvp_room_guests')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('room', models.ForeignKey(orm[u'rsvp.room'], null=False)),
            ('guest', models.ForeignKey(orm[u'rsvp.guest'], null=False))
        ))
        db.create_unique(m2m_table_name, ['room_id', 'guest_id'])

        # Deleting field 'Events.event_name'
        db.delete_column(u'rsvp_events', 'event_name')

        # Adding field 'Events.name'
        db.add_column(u'rsvp_events', 'name',
                      self.gf('django.db.models.fields.CharField')(default='Event', max_length=255),
                      keep_default=False)

        # Adding field 'Events.location'
        db.add_column(u'rsvp_events', 'location',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rsvp.Locations'], null=True),
                      keep_default=False)

        # Adding M2M table for field guests on 'Events'
        m2m_table_name = db.shorten_name(u'rsvp_events_guests')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('events', models.ForeignKey(orm[u'rsvp.events'], null=False)),
            ('guest', models.ForeignKey(orm[u'rsvp.guest'], null=False))
        ))
        db.create_unique(m2m_table_name, ['events_id', 'guest_id'])

        # Adding field 'Guest.primary'
        db.add_column(u'rsvp_guest', 'primary',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Guest.relation'
        db.add_column(u'rsvp_guest', 'relation',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rsvp.Guest'], null=True),
                      keep_default=False)

        # Deleting field 'Table.theme'
        db.delete_column(u'rsvp_table', 'theme')

        # Deleting field 'Table.guest_count'
        db.delete_column(u'rsvp_table', 'guest_count')

        # Adding field 'Table.name'
        db.add_column(u'rsvp_table', 'name',
                      self.gf('django.db.models.fields.CharField')(default='Table', max_length=255),
                      keep_default=False)

        # Adding M2M table for field guests on 'Table'
        m2m_table_name = db.shorten_name(u'rsvp_table_guests')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('table', models.ForeignKey(orm[u'rsvp.table'], null=False)),
            ('guest', models.ForeignKey(orm[u'rsvp.guest'], null=False))
        ))
        db.create_unique(m2m_table_name, ['table_id', 'guest_id'])


    def backwards(self, orm):
        # Deleting model 'Locations'
        db.delete_table(u'rsvp_locations')

        # Deleting model 'Hotel'
        db.delete_table(u'rsvp_hotel')

        # Removing M2M table for field guests on 'Hotel'
        db.delete_table(db.shorten_name(u'rsvp_hotel_guests'))

        # Deleting model 'Room'
        db.delete_table(u'rsvp_room')

        # Removing M2M table for field guests on 'Room'
        db.delete_table(db.shorten_name(u'rsvp_room_guests'))


        # User chose to not deal with backwards NULL issues for 'Events.event_name'
        raise RuntimeError("Cannot reverse this migration. 'Events.event_name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Events.event_name'
        db.add_column(u'rsvp_events', 'event_name',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)

        # Deleting field 'Events.name'
        db.delete_column(u'rsvp_events', 'name')

        # Deleting field 'Events.location'
        db.delete_column(u'rsvp_events', 'location_id')

        # Removing M2M table for field guests on 'Events'
        db.delete_table(db.shorten_name(u'rsvp_events_guests'))

        # Deleting field 'Guest.primary'
        db.delete_column(u'rsvp_guest', 'primary')

        # Deleting field 'Guest.relation'
        db.delete_column(u'rsvp_guest', 'relation_id')


        # User chose to not deal with backwards NULL issues for 'Table.theme'
        raise RuntimeError("Cannot reverse this migration. 'Table.theme' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Table.theme'
        db.add_column(u'rsvp_table', 'theme',
                      self.gf('django.db.models.fields.CharField')(max_length=45),
                      keep_default=False)

        # Adding field 'Table.guest_count'
        db.add_column(u'rsvp_table', 'guest_count',
                      self.gf('django.db.models.fields.IntegerField')(default=8),
                      keep_default=False)

        # Deleting field 'Table.name'
        db.delete_column(u'rsvp_table', 'name')

        # Removing M2M table for field guests on 'Table'
        db.delete_table(db.shorten_name(u'rsvp_table_guests'))


    models = {
        u'rsvp.events': {
            'Meta': {'object_name': 'Events'},
            'guests': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['rsvp.Guest']", 'null': 'True', 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsvp.Locations']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rsvp.guest': {
            'Meta': {'ordering': "['-last_name', '-first_name']", 'object_name': 'Guest'},
            'attending': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'max_guests': ('django.db.models.fields.IntegerField', [], {}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsvp.Guest']", 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'street_addr': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'max_length': '5'})
        },
        u'rsvp.hotel': {
            'Meta': {'object_name': 'Hotel'},
            'guests': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['rsvp.Guest']", 'null': 'True', 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rsvp.locations': {
            'Meta': {'object_name': 'Locations'},
            'distance': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rsvp.room': {
            'Meta': {'object_name': 'Room'},
            'guests': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['rsvp.Guest']", 'null': 'True', 'symmetrical': 'False'}),
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsvp.Hotel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_occupancy': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rsvp.table': {
            'Meta': {'object_name': 'Table'},
            'guests': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['rsvp.Guest']", 'null': 'True', 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['rsvp']