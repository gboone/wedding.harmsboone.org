from django.contrib import admin
from rsvp.models import Guest, Location, Table, Event, Hotel, Room, Party

class AdminModel(admin.ModelAdmin):
	list_display = ['name']

class GuestAdmin(admin.ModelAdmin):
	list_display = ['last_name', 'first_name']
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

class RoomAdmin(admin.ModelAdmin):
	list_display = ['name', 'hotel']

class PartyAdmin(admin.ModelAdmin):
	pass


admin.site.register(Guest, GuestAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Party, PartyAdmin)