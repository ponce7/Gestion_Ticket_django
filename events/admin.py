from django.contrib import admin

from events.models import Event, Recevoir, Ticket
# Register your models here.


admin.site.register(Event)

admin.site.register(Recevoir)

admin.site.register(Ticket)
