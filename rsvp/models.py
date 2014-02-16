from django.db import models
from django.forms import ModelForm
import datetime

class Guest(models.Model):		# we create a model for a single guest
	first_name = models.CharField(max_length=45, null=True, blank=True)
	last_name = models.CharField(max_length=45, null=True, blank=True)
	attending = models.BooleanField(blank=True)
	primary_email = models.EmailField(max_length=254, null=True, blank=True)
	street_addr = models.CharField(max_length=255, null=True, blank=True)
	city = models.CharField(max_length=255, null=True, blank=True)
	state = models.CharField(max_length=2, null=True, blank=True)
	zip_code = models.IntegerField(max_length=5, null=True, blank=True)
	primary = models.NullBooleanField(null=True, blank=True)
	events = models.ManyToManyField('Event', null=True, blank=True)
	hotel = models.ForeignKey('Hotel', null=True, blank=True)
	bride = models.BooleanField(default=False)
	groom = models.BooleanField(default=False)

	class Meta:
		ordering = ['-last_name', '-first_name']

	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class Abstract(models.Model):
	name = models.CharField(max_length=255)

	class Meta:
		abstract = True

	def __unicode__(self):
		return u'%s' % self.name 

class Location(models.Model):
	name = models.CharField(max_length=255)
	distance = models.DecimalField(decimal_places=1, max_digits=3)

	def __unicode__(self):
		return u'%s' % self.name

class Table(Abstract):
	pass

class Event(Abstract):
	location = models.ForeignKey(Location, null=True)
	notes = models.TextField(blank=True, null=True)
	date = models.DateTimeField(default=datetime.datetime(2014, 8, 1, 00))

class Hotel(Abstract):
	total_guest_count = models.IntegerField(max_length=2, null=True, blank=True)
	url = models.URLField(null=True, blank=True)
	notes = models.TextField()

class Roomtype(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return u'%s' % self.name

class Room(Abstract):
	hotel = models.ForeignKey(Hotel)
	max_occupancy = models.IntegerField()
	room_type = models.ForeignKey(Roomtype, null=True, blank=True)

class Party(models.Model):
	name = models.TextField(null=True, blank=True)
	guests = models.ManyToManyField(Guest)
	max_size = models.IntegerField(default=1)
	responded = models.BooleanField(default=False)

	def __unicode__(self):
		return u'%s' % self.name

class Song(models.Model):
	title = models.CharField(max_length=500)
	artist = models.CharField(max_length=500)
	comment = models.TextField(blank=True, null=True)
	requested_by = models.ManyToManyField(Guest, null=True, blank=True)
	votes = models.IntegerField(default=1)

	def __unicode__(self):
		return u'%s, %s' % (self.title, self.artist)