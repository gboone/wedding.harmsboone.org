
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.conf import settings
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory, BaseModelFormSet
from django.contrib.formtools.wizard.views import CookieWizardView
import datetime
from rsvp.models import Guest, Hotel, Event, Room, Party
from rsvp.forms import SongRequest, GuestAuth, GuestForm, GuestAttending, GuestHotelForm

def RequestView(request):
	RequestFormSet = formset_factory(SongRequest, max_num=5)
	if request.method == 'POST':
		formset = RequestFormSet(request.POST, request.FILES)
		if formset.is_valid():
			pass
	else:
		formset = RequestFormSet()
	return render(request, 'request.html', { 'formset' : formset })

def GuestAuthView(request):
	if request.method == 'POST':
		form = GuestAuth(request.POST)
		if form.is_valid():
			first = form.cleaned_data['first_name']
			last = form.cleaned_data['last_name']
			zip_code = form.cleaned_data['zip_code']
			primary = form.cleaned_data['key_value']
			key = first + last + str(zip_code) + str(primary)
			c = Guest.objects.get(pk=primary) 
			c_first = c.first_name
			c_last = c.last_name
			c_zip = str(c.zip_code)
			check = c_first + c_last + c_zip + str(c.pk)
			import hashlib
			key = hashlib.sha224(key).hexdigest()
			check = hashlib.sha224(check).hexdigest()
			if key == check:
				return HttpResponseRedirect('attending/?first_name=%s&last_name=%s&zip_code=%s&pk=%s' % ( first, last, zip_code, primary ))
	else:
		form = GuestAuth()

	return render(request, 'auth.html', {
		'form' : form,
	})

def GuestAttendanceView(request):
	get_vals = request.GET
	pk = get_vals['pk']
	guest = Guest.objects.get(pk=pk)
	party = guest.party_set.all()[0]
	size = party.max_size
	partyFormset = modelformset_factory(Guest, fields=['first_name', 'last_name', 'attending'], max_num=size)
	if request.method == 'POST':
		partyForm = partyFormset(request.POST)
		if partyForm.is_valid():
			partyForm = partyForm.save()
			return HttpResponseRedirect('yes/?pk=%s' % (pk))

	elif request.method == 'GET':
		partyForm = partyFormset(queryset=party.guests.all())

	return render(request, 'attending.html', {
		'partyForm' : partyForm,
		'guest' : guest
	})

def GuestVerifyView(request):
	pk = request.GET['pk']
	guest = Guest.objects.get(pk=pk)
	party = guest.party_set.all()[0]

	if request.method == 'POST':
		guestform = GuestHotelForm(request.POST, instance=guest)
		if guestform.is_valid():
			guestform = guestform.save()
			return HttpResponseRedirect('confirm/')

	elif request.method == 'GET':
		guestform = GuestHotelForm(instance=guest)
	else:
		GuestHotelForm()

	return render(request, 'request.html', {
		'guestform' : guestform,
		'guest' : guest,
		'party' : party,
	})

def GuestConfirmView(request):
	referrer = request.META['HTTP_REFERER']
	index = referrer.index('=')
	pk = referrer[index + 1:]
	guest = Guest.objects.get(pk=pk)
	events = guest.events.all()
	party = guest.party_set.all()[0]
	members = party.guests.all()

	return render(request, 'confirm.html', {
		'guest' : guest,
		'events' : events,
		'party' : party,
		'members' : members
		} )