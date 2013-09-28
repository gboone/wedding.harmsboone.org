from django.shortcuts import render, get_object_or_404
from mysite.models import Post

def index(request):
	# get the blog posts that are published
	home = Post.objects.get(slug='home')
	#now return the rendered template
	return render(request, 'index.html', {'posts':home})

# def location(request):
# 	#get the Post
# 	# post = get_object_or_404(Post, slug=request)
# 	post = Post.objects.get(slug='location')
# 	#return the rendered template
# 	return render(request, 'post.html', {'post': post})

# def directions(request):
# 	#get the Post
# 	# post = get_object_or_404(Post, slug=request)
# 	post = Post.objects.get(slug='directions')
# 	#return the rendered template
# 	return render(request, 'post.html', {'post': post})

def page(request, string):
	#get the Post
	post = Post.objects.get(slug=string)
	#return the rendered template
	return render(request, 'post.html', {'post' : post})