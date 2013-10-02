from django.contrib import admin
from mysite.models import Post
from rsvp.models import Guest

class PostAdmin(admin.ModelAdmin):
	#fields display on change list
	list_display = ['title', 'description']
	#fields to filter the change list with
	list_filter = ['published', 'created']
	#fields to search in change list
	search_fields = ['title', 'description', 'content']
	#enable the date drill down on change list
	date_hierarchy = 'created'
	#enable the save buttons on top of change form
	save_on_top = True
	#prepopulate the slug from the title
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post)

class GuestAdmin(admin.ModelAdmin):
	list_display = ['last_name', 'first_name']
	list_filter = ['last_name', 'first_name']
	search_fields = ['last_name', 'first_name', ]
	save_on_top = True

admin.site.register(Guest)