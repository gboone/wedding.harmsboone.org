from django.db import models

class Guest(models.Model):		# we create a model for a single guest
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	prefix = models.CharField(max_length=4)
	max_guests = models.IntegerField()
	attending = models.BooleanField()
	primary_email = models.EmailField(max_length=254)
	street_addr = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=2)
	zip_code = models.IntegerField(max_length=5)

	class Meta:
		ordering = ['-last_name', '-first_name']

	def __unicode__(self):
		return u'%s, %s' % (self.last_name, self.first_name)

class FamilyMember():
	family = models.ForeignKey(Guest)

class Table(models.Model):
	guest_count = models.IntegerField()
	theme = models.CharField(max_length=45)

class Events(models.Model):
	event_name = models.CharField(max_length=255)