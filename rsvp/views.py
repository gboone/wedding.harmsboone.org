
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.conf import settings
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory, BaseModelFormSet
from django.contrib.formtools.wizard.views import CookieWizardView
import datetime

from rsvp.models import Guest, Hotel, Event, Room
from rsvp.forms import ContactForm, SongRequest, GuestAuth, GuestVerify, GuestAttending, GuestNamesVerify, HotelChooser
from rsvp.forms import RoomChooser, EventChooser, ChippewaYepnope, ChippewaData
def ContactView(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			cc_myself = form.cleaned_data['cc_myself']

			recipients = ['boone.greg@gmail.com']
			if cc_myself:
				recipients.append(sender)

			from django.core.mail import send_mail
			send_mail(subject, message, sender, recipients)
			return HttpResponseRedirect('/')
	else:
		form = ContactForm()

	return render(request, 'contact.html', {
		'form' : form,
	})

def show_message_from_condition(wizard):
	cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
class RsvpWizard(CookieWizardView):
	def done(self, form_list, **kwargs):
		return HttpResponseRedirect('/complete')

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
				return HttpResponseRedirect('yes/?first_name=%s&last_name=%s&zip_code=%s&pk=%s' % ( first, last, zip_code, primary ))
	else:
		form = GuestAuth()

	return render(request, 'auth.html', {
		'form' : form,
	})

def GuestVerifyView(request):
	if not request.GET['pk']:
		HttpResponseForbidden
	elif request.method == 'GET':
		get_vals = request.GET
		pk = get_vals['pk']
		guest = Guest.objects.get(pk=pk)
		first = guest.first_name
		last = guest.last_name
		yepnope = [guest]
		GuestNameFormset = modelformset_factory(Guest, fields=['first_name', 'last_name'], extra=1, max_num=guest.max_guests)
		EventFormset = modelformset_factory(Event, fields=['name'])
		hotels = Hotel.objects
		if guest.attending == True:
			greeting = u'Looks like you are already coming!'
			yepnope = u'Thanks for RSVPing, see you in August!'
		else:
			greeting = 'Will you be able to join us for the wedding on August 16?'
			yepnope = GuestAttending(yepnope)
			if guest.primary == True: # if this is a primary guest (the one on the invite)
				query = Guest.objects.filter(relation=guest.pk)
				max_guests = guest.max_guests
				formset = GuestNameFormset(queryset=query)
			else:
				relative = Guest.objects.get(relation=guest.relation)
				query = Guest.objects.filter(relation=relative)
				max_guests = relative.max_guests
				formset = GuestNameFormset(queryset=query)
			hotel_yepnope = ChippewaYepnope()
			chip_data = ChippewaData()
			hotel_form = HotelChooser()
			room_form = RoomChooser()
			eventform = EventChooser()

			# hotel_form = Hotel.objects.get(guests=guest)

			# hotel_form = HotelChooser()
	# elif request.method == 'POST'
	# 	pass
	# 	forms = ( yepnope, formset )
	# 	for form in forms:
	# 		if is_valid(form):
	# 			# Anything we're doing before we save.
	# 		else:
	# 			break
	else:
		formset = GuestNameFormset()

	return render(request, 'request.html', {
		'greeting' : greeting,
		'formset' : formset,
		'yepnope' : yepnope,
		'first_name' : first,
		'last_name' : last,
		'hotel_yepnope' : hotel_yepnope,
		'chip_data' : chip_data,
		'hotel_form' : hotel_form,
		'room_form' : room_form,
		'event_form' : eventform,
	})
	# elif request.method == 'POST':
	# 	pass
	# else:
	# 	form = GuestAuth()

	# return render(request, 'request.html', {
	# 	'formset' : formset,
	# })
# def rsvp(request):
# 	if request.method == 'POST':
# 		form = 
# 		if form.is_valid():
# 			first = form.cleaned_data['first_name']
# 			second = form.cleaned_data['last_name']
# 			third = form.cleaned_data['zip_code']
# 			complete = first + second + third
# 			check = Guest
# 			if complete = Guest.