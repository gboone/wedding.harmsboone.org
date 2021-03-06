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

class Event(models.Model):
	name = models.CharField(max_length=255)
	location = models.ForeignKey(Location, null=True)
	notes = models.TextField(blank=True, null=True)
	date = models.DateTimeField(default=datetime.datetime(2014, 8, 1, 00))

	class Meta:
		ordering = ['date']

	def __unicode__(self):
		date = self.date.strftime("%A")
		name = self.name
		return u'%s: %s' % (date, name)

class Hotel(Abstract):
	total_guest_count = models.IntegerField(max_length=2, null=True, blank=True)
	url = models.URLField(null=True, blank=True)
	notes = models.TextField()
	block = models.BooleanField(default=False, blank=True)

class Party(models.Model):
	name = models.TextField(null=True, blank=True)
	guests = models.ManyToManyField(Guest)
	max_size = models.IntegerField(default=1)
	responded = models.BooleanField(default=False)
	gift = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return u'%s' % self.name

class Song(models.Model):
	title = models.CharField(max_length=500)
	artist = models.CharField(max_length=500)
	comment = models.TextField(blank=True, null=True)
	requested_by = models.ManyToManyField(Guest, null=True, blank=True)
	votes = models.IntegerField(default=1)

	def __unicode__(self):
		return u'%s, %s' % (self.title.capitalize(), self.artist.capitalize())