from django.contrib import admin

from .models import Room, Booking


# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    pass


admin.site.register(Room, RoomAdmin)


class BookingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Booking, RoomAdmin)
