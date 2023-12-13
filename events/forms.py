from django import forms
from .models import Event, Recevoir



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'lieu', 'event_date', 'event_photo', 'nbr_ticket', 'price')


class RecevoirForm(forms.ModelForm):
    class Meta:
        model = Recevoir
        fields = ("email", "qte")
        