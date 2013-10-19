
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.conf import settings
from django.forms.formsets import formset_factory

from rsvp.forms import ContactForm, SongRequest

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

def RequestView(request):
	RequestFormSet = formset_factory(SongRequest, max_num=5)
	if request.method == 'POST':
		formset = RequestFormSet(request.POST, request.FILES)
		if formset.is_valid():
			pass
	else:
		formset = RequestFormSet()
	return render_to_response('request.html', { 'formset' : formset })

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