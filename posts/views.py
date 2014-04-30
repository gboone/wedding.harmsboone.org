from django.shortcuts import render, get_object_or_404
from posts.models import Post
from rsvp.models import Guest, Party, Hotel, Event

def index(request):
	# get the blog posts that are published
	home = Post.objects.get(slug='home')
	bride = Guest.objects.get(bride=True)
	groom = Guest.objects.get(groom=True)
	#now return the rendered template
	return render(request, 'index.html', {
		'posts':home,
		'bride' : bride,
		'groom' : groom
	})

def page(request, string):
	#get the Post
	post = Post.objects.get(slug=string)
	bride = Guest.objects.get(bride=True)
	groom = Guest.objects.get(groom=True)
	#return the rendered template
	return render(request, 'post.html', {
		'post' : post,
		'bride' : bride,
		'groom' : groom,
	})

def thanks(request):
	post = Post.objects.get(slug='thanks')
	pk = request.session.get('pk')
	guest = Guest.objects.get(pk=pk)
	bride = Guest.objects.get(bride=True)
	groom = Guest.objects.get(groom=True)
	party = guest.party_set.all()[0]
	if (party.pk is not None):
		party.responded = True
		party.save()
	request.session.flush()
	return render(request, 'post.html', {
		'attending' : guest.attending,
		'post' : post,
 		'bride' : bride,
		'groom' : groom,
	})

def lodging(request):
	main = Hotel.objects.get(pk=1)
	other = Hotel.objects.get(name='Other')
	objects = Hotel.objects.all().exclude(pk=main.pk).exclude(pk=other.pk)
	bride = Guest.objects.get(bride=True)
	groom = Guest.objects.get(groom=True)
	return render(request, 'from-objects.html', {
		'bride' : bride,
		'groom' : groom,
		'main' : main,
		'objects' : objects,
		'class' : 'stock',
		'heading' : 'Where to Stay',
		'subheading' : 'Other options',
	})

def activities(request):
	bride = Guest.objects.get(bride=True)
	groom = Guest.objects.get(groom=True)
	main = Event.objects.get(pk=1)
	objects = Event.objects.all().exclude(pk=main.pk)
	page = Post.objects.get(slug='activities')
	return render(request, 'date-objects.html', {
		'bride' : bride,
		'groom' : groom,
		'main' : main,
		'objects' : objects.order_by('date'),
		'class' : 'goose',
		'heading' : 'Weekend Activities',
		'page' : page,
		'subheading' : 'Extras'
		})