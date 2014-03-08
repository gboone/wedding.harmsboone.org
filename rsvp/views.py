import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseServerError, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.conf import settings
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory, BaseModelFormSet
from django.contrib.formtools.wizard.views import CookieWizardView
from rsvp.models import Guest, Hotel, Event, Room, Party, Song
from rsvp.forms import SongRequest, GuestAuth, GuestForm, GuestAttending
from rsvp.forms import GuestHotelForm, GuestChoice, PartyChoice
from django.views.decorators.cache import cache_page
bride = Guest.objects.get(bride=True)
groom = Guest.objects.get(groom=True)

@cache_page(60, cache='default', key_prefix='rsvp')
def GuestAuthView(request):
	global bride
	global groom
	if request.session.get('pk') is not None:
		return HttpResponseRedirect('attending/')
	if request.method == 'POST':
		form = GuestAuth(request.POST)
		if form.is_valid():
			first = form.cleaned_data['first_name']
			last = form.cleaned_data['last_name']
			zip_code = form.cleaned_data['zip_code']
			party = form.cleaned_data['key_value']
			key = first + last + str(zip_code) + str(party)
			c = Guest.objects.get(first_name=first, last_name=last) 
			c_first = c.first_name
			c_last = c.last_name
			c_zip = str(c.zip_code)
			c_party = c.party_set.all()
			check = c_first + c_last + c_zip + str(c_party[0].pk)
			import hashlib
			key = hashlib.sha224(key).hexdigest()
			check = hashlib.sha224(check).hexdigest()
			if key == check:
				request.session['pk'] = c.pk
				return HttpResponseRedirect('attending/')
	else:
		form = GuestAuth()

	return render(request, 'auth.html', {
		'form' : form,
		'bride' : bride,
		'groom' : groom,
	})

@cache_page(60, cache='default', key_prefix='rsvp')
def GuestAttendanceView(request):
	global bride
	global groom
	pk = request.session.get('pk')
	guest = Guest.objects.get(pk=pk)
	party = guest.party_set.all()[0]
	size = party.max_size
	partyFormset = modelformset_factory(Guest,
		fields=['first_name', 'last_name', 'attending'],
		max_num=size
	)
	if request.method == 'POST':
		partyForm = partyFormset(request.POST)
		if partyForm.is_valid():
			partyForm = partyForm.save()
			return HttpResponseRedirect('yes/')

	elif request.method == 'GET':
		partyForm = partyFormset(queryset=party.guests.all())

	return render(request, 'attending.html', {
		'partyForm' : partyForm,
		'guest' : guest,
		'bride' : bride,
		'groom' : groom,
	})

@cache_page(60, cache='default', key_prefix='rsvp')
def GuestVerifyView(request):
	global bride
	global groom
	pk = request.session.get('pk')
	guest = Guest.objects.get(pk=pk)
	party = guest.party_set.all()[0]
	others = Guest.objects.filter(party=party.pk)
	if request.method == 'POST':
		guestform = GuestHotelForm(request.POST, instance=guest)
		if guestform.is_valid():
			guestform = guestform.save()
			events = guest.events.all()
			for other in others:
				other.hotel = guest.hotel
				other.street_addr = guest.street_addr
				other.city = guest.city
				other.state = guest.state
				other.zip_code = guest.zip_code
				for event in events:
					other.events.add(event.pk)
				other.save()
			return HttpResponseRedirect('request/')

	elif request.method == 'GET':
		guestform = GuestHotelForm(instance=guest)
	else:
		guestform = GuestHotelForm()

	return render(request, 'logistics.html', {
		'guestform' : guestform,
		'guest' : guest,
		'party' : party,
		'bride' : bride,
		'groom' : groom,
	})

@cache_page(60, cache='default', key_prefix='rsvp')
def RequestView(request):
	global bride
	global groom
	pk = request.session.get('pk')
	guest = Guest.objects.get(pk=pk)
	RequestFormSet = modelformset_factory(
		Song,
		fields=['title', 'artist'],
		max_num=5, extra=5
	)
	if request.method == 'POST':
		formset = RequestFormSet(request.POST)
		if formset.is_valid():
			objects = formset.save(commit=False)
			for song in objects:
				requested = Song.objects.filter(
					title=song.title,
					artist=song.artist
				)
				if len(requested) == 1:
					song = Song.objects.get(
						title=song.title,
						artist=song.artist
					)
				else:
					song = Song.objects.create(
						title=song.title,
						artist=song.artist
					)
				song.requested_by.add(guest)
				song.votes = song.requested_by.count()
				song.save()
		return HttpResponseRedirect('confirm/');
	else:
		requested = Song.objects.filter(requested_by=Guest.objects.get(pk=pk))
		if len(requested) > 0:
			formset = RequestFormSet(queryset=requested)
		else:
			formset = RequestFormSet(queryset=Song.objects.filter(id=0))
	return render(request, 'request.html', { 
		'formset' : formset,
		'bride' : bride,
		'groom' : groom,
	 })

@cache_page(60, cache='default', key_prefix='rsvp')
def GuestConfirmView(request):
	global bride
	global groom
	pk = request.session.get('pk')
	guest = Guest.objects.get(pk=pk)
	events = guest.events.all()
	party = guest.party_set.all()[0]
	members = party.guests.all()
	block = Hotel.objects.filter(block=True)
	block = block[0]
	return render(request, 'confirm.html', {
		'guest' : guest,
		'events' : events,
		'party' : party,
		'members' : members,
		'bride' : bride,
		'bride' : bride,
		'groom' : groom,
		'block' : block,
		} )

def ReportView(request):
	global bride
	global groom
	guests = GuestChoice()
	parties = PartyChoice()
	return render(request, 'report-landing.html', {
		'guests' : guests,
		'parties' : parties,
		'bride' : bride,
		'groom' : groom,
		})