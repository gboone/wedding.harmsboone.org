# forms.py
from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(
		widget=forms.TextInput(attrs={'rows':'80', 'cols':'20'}))
	sender = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)

class SongRequest(forms.Form):
	artist = forms.CharField()
	song = forms.CharField()

