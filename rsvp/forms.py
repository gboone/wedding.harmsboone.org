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

class GuestAuth(forms.Form):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	zip_code = forms.IntegerField()
	attending = forms.BooleanField(required=False)

# class GuestNameVerify(forms.Form):
# 	for relation as guest_name
# 		name = forms.CharField(max_length=100)
