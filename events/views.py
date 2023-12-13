import base64
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.urls import reverse
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *

from django.utils import timezone

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.mail import send_mail, EmailMessage


from django.core.mail import EmailMessage, get_connection
from django.conf import settings


from django.http import HttpResponse


from .pdf import html2pdf

from django.core.mail import EmailMessage

from django.forms import ModelForm
from .forms import EventForm


import io


from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa 
from unittest import result

# Create your views here.
def index(request):
    events = Event.objects.all()
   
    return render(request, "events/index.html", context={'events': events})

@login_required
def add_event(request):  
        if request.method == "POST":
                name = request.POST.get("name")
                lieu = request.POST.get("lieu")
                event_date = request.POST.get("event_date")
                nbr_ticket = request.POST.get("nbr_ticket")
                price = request.POST.get("price")
              
                if datetime.strptime(event_date, "%Y-%m-%dT%H:%M") <= datetime.now():
                    message = "La date ou l'heure ne doivent pas etre anterieur a la date d'aujourd'hui."
                    return render(request, 'events/event.html', {'message':message})
                if len(request.FILES) != 0:
                    event_photo = request.FILES["event_photo"]

                else:
                     return render(request, 'events/event.html') 
                my_event=Event.objects.create(name=name, lieu=lieu, event_date=event_date, event_photo=event_photo, nbr_ticket=nbr_ticket, price=price)
                my_event.save()
                return redirect("index")
        else:
            return render(request, 'events/event.html')
    
def commande(request, id):
   
    events = Event.objects.get(id=id)
    event = get_object_or_404(Event, id=id)
    
    product = Event.objects.get(id=id)
   
    
    if request.method == "POST":
        qte = request.POST.get("qte")
        email = request.POST.get("email")
        form = RecevoirForm(request.POST)
        elmt = int(request.POST['qte'])
       
        if (elmt > event.nbr_ticket):
            message ="Attention passez une commande en dessous de ce nombre."
            return render(request, 'events\commande.html' , {'message':message, 'form': RecevoirForm, 'events': events})
        
        if (elmt < 0):
            message ="Attention pas de commande inférieur à 0 ."
            return render(request, 'events\commande.html' , {'message':message, 'form': RecevoirForm, 'events': events})
        
        if form.is_valid:
            product.nbr_ticket = product.nbr_ticket - int(request.POST['qte'])
            product.save()
            form.save()


            #Envoie de mail
            nbr_email = int(request.POST.get('qte'))
            #Create list for multiplicate email
            crt_liste = []
            for _ in range(nbr_email):
                crt_liste.append(0)

            subject = "Bon d'achat ticket"
            message_contenu = "PDF contenu"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = request.POST.get('email')
            mail = EmailMessage(subject, message_contenu, from_email, [recipient_list])
        
            context = {
                    'events':events,
                    'qte':crt_liste,
                    'obj': generateQrCode("http://127.0.0.1:8000/pdf/")
                    
                }
            pdf_var = html2pdf("events/pdf.html",context)
            filename = event.name + ".pdf"
                
            mail.attach(filename, pdf_var, 'application/pdf') 
                
            
            
            mail.send()
            return render(request,'events/test.html', {'events':events, 'qte':range(nbr_email)})
        
        else:
            return render(request, 'events/commande.html', {'form': RecevoirForm , 'events': events})
    return render(request, 'events/commande.html', {'form': RecevoirForm, 'events':events})

def pdf(request, id):
    events = Event.objects.get(id=id)
    context = {
        'events':events,
        'obj': generateQrCode("http://127.0.0.1:8000/pdf/"),
     }
    pdf_var = html2pdf("events/pdf.html",context)
    return HttpResponse(pdf_var, content_type="application/pdf")

def pdf_copie(request):
    events = Event.objects.get(id=7)
    return render(request, "events/pdf.html", context={'events': events})

def generateQrCode(data):
     # Generate the QR code image
     qr = qrcode.QRCode(version=1, box_size=10, border=5)

     #data = 'https://example.com'
     qr.add_data(data)
     qr.make(fit=True)
     img = qr.make_image(fill='black', back_color='white')

     # Convert the image to a base64-encoded string

     buffer = BytesIO()
     img.save(buffer, format='PNG')
     img_str = base64.b64encode(buffer.getvalue()).decode()

     return img_str