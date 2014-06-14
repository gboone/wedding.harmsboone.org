from django.contrib import admin
from django.utils import html
from rsvp.models import Guest, Location, Table, Event, Hotel, Party, Song

class AdminModel(admin.ModelAdmin):
	list_display = ['name']

class GuestAdmin(admin.ModelAdmin):
	list_display = ['last_name', 'first_name', 'attending', ]
	list_filter = ['last_name', 'first_name']
	search_fields = ['last_name', 'first_name', ]
	save_on_top = True

class LocationAdmin(AdminModel):
	pass

class TableAdmin(AdminModel):
	pass

class EventAdmin(admin.ModelAdmin):
	
	def guest_count(self, request):
		guest_count = Event.objects.get(pk=request.pk).guest_set.count()	
		return guest_count

	def guests(self, request):
		guests = Event.objects.get(pk=request.pk).guest_set.order_by('last_name')
		guest_count = guests.count()
		guest_list = """
		<p>Guest count = %d
		Guests are listed below
		<ul>
		""" % Event.objects.get(pk=request.pk).guest_set.count()
		for g in guests:
			guest_list = guest_list + "<li>%s %s</li>" % (g.first_name, g.last_name)
		
		guest_list = guest_list + "</ul></p>"
		guest_list = html.format_html(guest_list)
		return guest_list

	list_display = ['name', 'guest_count']
	readonly_fields = ['guests']
	pass

class HotelAdmin(AdminModel):
	pass

class PartyAdmin(admin.ModelAdmin):
    filter_horizontal = ('guests',)
    list_display = ['name', 'responded']
    list_display_links = ['responded']

class SongAdmin(admin.ModelAdmin):
	list_display = ['title', 'artist', 'votes']

admin.site.register(Guest, GuestAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Party, PartyAdmin)
admin.site.register(Song, SongAdmin)