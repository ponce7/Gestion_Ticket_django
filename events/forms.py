from django import forms
from events.models import Event, Recevoir



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'lieu', 'event_date', 'nbr_ticket')


class RecevoirForm(forms.ModelForm):
    class Meta:
        model = Recevoir
        fields = ("email", "qte")
        