from django.shortcuts import render, get_object_or_404
from posts.models import Post

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