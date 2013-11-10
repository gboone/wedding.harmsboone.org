from django.db import models
from django.forms import ModelForm

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

	class Meta:
		ordering = ['-last_name', '-first_name']

	def __unicode__(self):
		return u'%s, %s' % (self.last_name, self.first_name)

class Abstract(models.Model):
	name = models.CharField(max_length=255)
	guests = models.ManyToManyField(Guest, null=True)

	class Meta:
		abstract = True

	def __unicode__(self):
		return u'%s' % self.name 

class Location(models.Model):
	name = models.CharField(max_length=255)
	distance = models.IntegerField()

	def __unicode__(self):
		return u'%s' % self.name

class Table(Abstract):
	pass

class Event(Abstract):
	location = models.ForeignKey(Location, null=True)

class Hotel(Abstract):
	pass

class Room(Abstract):
	hotel = models.ForeignKey(Hotel)
	max_occupancy = models.IntegerField()


