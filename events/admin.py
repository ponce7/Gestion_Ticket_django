from django.contrib import admin

from events.models import Event, Recevoir, Ticket, SubscribedUsers, Newsletter, Organisateur
# Register your models here.

# class SubscribeUsersAdmin(admin.ModelAdmin):
#     list_display = ('email', 'created_date')



admin.site.register(Event)

admin.site.register(Recevoir)

admin.site.register(Ticket)

admin.site.register(SubscribedUsers)

admin.site.register(Newsletter)

admin.site.register(Organisateur)