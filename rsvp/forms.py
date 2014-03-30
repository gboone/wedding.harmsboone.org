# forms.py
from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory, BaseModelFormSet
import html5.forms.widgets as html5_widgets
from rsvp.models import Guest, Hotel, Event, Party, Song

forms.DateInput.input_type="date"
forms.DateTimeInput.input_type="datetime-local"

class SongRequest(ModelForm):
	class Meta:
		model = Song

class GuestAuth(forms.Form):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	zip_code = forms.IntegerField()
	invitation_number = forms.IntegerField()

class AttendanceForm(ModelForm):
	class Meta:
		model =Guest
		fields = ('first_name', 'last_name', 'attending')

class GuestAttending(ModelForm):
	class Meta:
		model = Guest
		fields = ['attending']

	attending = forms.BooleanField(label='Check the box if you are attending.')

class GuestForm(ModelForm):
	class Meta:
		model = Guest

class GuestHotelForm(ModelForm):
	class Meta:
		model = Guest
		exclude = ['zip_code', 'first_name', 'last_name', 'attending', 'primary_email', 'street_addr', 'city', 'state', 'primary', 'bride', 'groom']

class GuestChoice(forms.Form):
	guests = Guest.objects.all()
	guest = forms.ChoiceField(choices=guests)

class PartyChoice(forms.Form):
	parties = Party.objects.all()
	party = forms.ChoiceField(choices=parties)