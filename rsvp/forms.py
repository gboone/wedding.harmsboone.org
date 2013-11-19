# forms.py
from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory, BaseModelFormSet
from rsvp.models import Guest

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(
		widget=forms.TextInput(attrs={'rows':'80', 'cols':'20'}))
	sender = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)

class SongRequest(forms.Form):
	artist = forms.CharField()
	song = forms.CharField()

class GuestAuth(forms.Form):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	zip_code = forms.IntegerField()

class GuestAttending(ModelForm):
	class Meta:
		model = Guest
		fields = ['attending']

class GuestNamesVerify(ModelForm):
	class Meta:
		model = Guest

class GuestVerify(ModelForm):
	class Meta:
		model = Guest

	def __init__(self, data_from_post = None):
		if data_from_post is not None:
			_post = data_from_post
			first = _post.get('first_name', None)
			last = _post.get('last_name', None)
			primary = Guest.objects.get(first_name=first, last_name=last)

	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)