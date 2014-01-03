from django.db import models
from django.forms import ModelForm
import datetime

class Guest(models.Model):		# we create a model for a single guest
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	display_as = models.CharField(max_length= 91, null=True)
	prefix = models.CharField(max_length=4, null=True, blank=True)
	max_guests = models.IntegerField(default=0, null=True, blank=True)
	attending = models.BooleanField()
	primary_email = models.EmailField(max_length=254)
	street_addr = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=2)
	zip_code = models.IntegerField(max_length=5)
	primary = models.BooleanField()
	relation = models.ForeignKey('self', null=True, blank=True)
	arriving = models.DateField(default=datetime.date(2014, 8, 14).strftime("%Y-%m-%d"))
	departing = models.DateField(default=datetime.date(2014, 8, 17).strftime("%Y-%m-%d"))
	nights = models.IntegerField(max_length=1)
	notes = models.TextField(default="None", max_length=2048, null=True, blank=True)

	class Meta:
		ordering = ['-last_name', '-first_name']

	def __unicode__(self):
		return u'%s, %s' % (self.last_name, self.first_name)

class Abstract(models.Model):
	name = models.CharField(max_length=255)
	guests = models.ManyToManyField(Guest, null=True, blank=True)

	class Meta:
		abstract = True

	def __unicode__(self):
		return u'%s' % self.name 

class Location(models.Model):
	name = models.CharField(max_length=255)
	distance = models.DecimalField(decimal_places=2, max_digits=3)

	def __unicode__(self):
		return u'%s' % self.name

class Table(Abstract):
	pass

class Event(Abstract):
	location = models.ForeignKey(Location, null=True)

class Hotel(Abstract):
	total_guest_count = models.IntegerField(max_length=2, null=True, blank=True)
	hotel_url = models.URLField(null=True, blank=True)
	notes = models.TextField()

class Roomtype(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return u'%s' % self.name

class Room(Abstract):
	hotel = models.ForeignKey(Hotel)
	max_occupancy = models.IntegerField()
	room_type = models.ForeignKey(Roomtype, null=True, blank=True)