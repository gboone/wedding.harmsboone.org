from django.shortcuts import render, get_object_or_404
from posts.models import Post
from rsvp.models import Guest, Party, Hotel

def index(request):
	# get the blog posts that are published
	home = Post.objects.get(slug='home')
	#now return the rendered template
	return render(request, 'index.html', {'posts':home})

def page(request, string):
	#get the Post
	post = Post.objects.get(slug=string)
	#return the rendered template
	return render(request, 'post.html', {'post' : post})

def thanks(request):
	post = Post.objects.get(slug='thanks')
	pk = request.session.get('pk')
	guest = Guest.objects.get(pk=pk)
	party = guest.party_set.all()[0]
	if (party.pk is not None):
		party.responded = True
		party.save()
	request.session.flush()
	return render(request, 'post.html', {'post' : post})

def lodging(request):
	main = Hotel.objects.get(pk=1)
	objects = Hotel.objects.all().exclude(pk=main.pk)
	return render(request, 'from-objects.html', {
		'main' : main,
		'objects' : objects,
		'class' : 'stock',
		'heading' : 'Where to Stay',
		'subheading' : 'Other options',
	})

def events(request):
	main = Events.objects.get(pk=1)
	objects = Events.objects.all().exclude(pk=main.pk)
	return render(request, 'date-objects.html', {
		'main' : main,
		'objects' : objects,
		'class' : 'goose',
		'heading' : 'Weekend Activities',
		'subheading' : 'Other Activiies',
		})