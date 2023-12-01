from django.contrib import admin

from events.models import Event, Cart, Order, Recevoir
# Register your models here.


admin.site.register(Event)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Recevoir)