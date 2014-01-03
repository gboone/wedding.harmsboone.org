# forms.py
from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory, BaseModelFormSet
import html5.forms.widgets as html5_widgets
from rsvp.models import Guest, Hotel, Event, Room

forms.DateInput.input_type="date"
forms.DateTimeInput.input_type="datetime-local" 

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
	key_value = forms.IntegerField()

class GuestAttending(ModelForm):
	class Meta:
		model = Guest
		fields = ['attending']

	attending = forms.BooleanField(label='Check the box if you are attending.')

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

class ChippewaYepnope(forms.Form):
	stay_here = forms.ChoiceField(label = u'Do you want to stay at Chippewa Retreat?', widget=forms.RadioSelect, choices=((False, 'No'), (True, 'Yes')))

class ChippewaData(forms.ModelForm):
	class Meta:
		model = Guest
		exclude = ('first_name', 'last_name', 'display_as', 'prefix', 'max_guests', 'attending', 'primary_email', 'street_addr', 'city', 'state', 'zip_code', 'primary', 'relation', 'nights', 'notes')

	notes = forms.CharField(widget=forms.Textarea, label = u'Please write any notes about room preferences below.')

class HotelChooser(forms.ModelForm):
	class Meta:
		model = Hotel
		exclude = ('guests', 'total_guest_count', 'hotel_url', 'name', 'notes')

	hotel = forms.ModelChoiceField(queryset=Hotel.objects.order_by('pk'), empty_label=u"Other/Don't know.")

class RoomChooser(forms.ModelForm):
	class Meta:
		model = Room
		exclude= ('name','max_occupancy','room_type','hotel','guests')

	room = forms.ModelChoiceField(queryset=Room.objects.only('room_type'), empty_label=u"N/A: Not staying at Chippewa")

class EventChooser(ModelForm):
	class Meta:
		model = Event
		exclude = ('name', 'guests','location',)
		label = {'name': u'Select the events you want to attend',}

	events = forms.ModelMultipleChoiceField(queryset=Event.objects.exclude(pk=1), widget=forms.CheckboxSelectMultiple)