from django.contrib import admin
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

class EventAdmin(AdminModel):
	pass

class HotelAdmin(AdminModel):
	pass

class PartyAdmin(admin.ModelAdmin):
    filter_horizontal = ('guests',)
    list_display = ['name', 'responded']
class SongAdmin(admin.ModelAdmin):
	list_display = ['title', 'artist', 'votes']

admin.site.register(Guest, GuestAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Party, PartyAdmin)
admin.site.register(Song, SongAdmin)