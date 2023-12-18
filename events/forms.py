from django import forms
from .models import *



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'lieu', 'event_date', 'event_photo', 'nbr_ticket', 'price')


class RecevoirForm(forms.ModelForm):
    class Meta:
        model = Recevoir
        fields = ("email", "qte")
        

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = SubscribedUsers
        fields = ('email','created_date')


class NewsletterForm(forms.Form):
    subject = forms.CharField()
    #receivers = forms.CharField()
    message = forms.CharField( label="Email content")

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ("subject", "message")
        

class OrganisateurForm(forms.ModelForm):
    class Meta:
        model = Organisateur
        fields = ("name", "email", "password")
        exclude = ("eventy",)
        
