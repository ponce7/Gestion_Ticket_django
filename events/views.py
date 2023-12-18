import base64
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core.validators import validate_email
from django.core.exceptions import ValidationError



from django.core.paginator import Paginator


import qrcode 

from django.core.mail import EmailMessage


from django.core.mail import EmailMessage
from django.conf import settings


from django.http import HttpResponse


from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa 


from django.views.generic import TemplateView, ListView
from .models import Event
import json
from django.db.models import Q
from django.contrib.auth import  get_user_model



User = get_user_model()
# Create your views here.




def html2pdf(template_path, context_dict={}):
    template = get_template(template_path)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
    
    if not pdf.err:
        return result.getvalue()
    return None


def index(request):
    events = Event.objects.all()
    return render(request, "events/index.html", context={'events': events})



@login_required
def add_event(request, id):   
        if request.method == "POST":
                name = request.POST.get("name")
                lieu = request.POST.get("lieu")
                event_date = request.POST.get("event_date")
                nbr_ticket = request.POST.get("nbr_ticket")
                price = request.POST.get("price")
                id_user = id

                if int(nbr_ticket) <= 0:
                     message_error = "Entrez un nombre superieur a 0"
                     return render(request, 'events/event.html', {'message_error':message_error})
                if int(price) <= 0:
                     message_error1 = "Entrez un nombre superieur a 0"
                     return render(request, 'events/event.html', {'message_error1':message_error1})
              
                if datetime.strptime(event_date, "%Y-%m-%dT%H:%M") <= datetime.now():
                    message = "La date et l'heure ne doivent pas etre anterieur a la date d'aujourd'hui."
                    return render(request, 'events/event.html', {'message':message, 'id_user':id_user})
                if len(request.FILES) != 0:
                    event_photo = request.FILES["event_photo"]

                else:
                     return render(request, 'events/event.html') 
                my_event=Event.objects.create(name=name, lieu=lieu, event_date=event_date, event_photo=event_photo, nbr_ticket=nbr_ticket, price=price, id_user=id_user)
                my_event.save()
                return redirect("index")
        else:
            return render(request, 'events/event.html')
        
@login_required
def show_event(request, id):
    id_organisateur = User.objects.get(id=id)   
    events = Event.objects.filter(id_user=id)
    return render(request, "events/show.html", context={'events': events, 'id_organisateur':id_organisateur})
  


 
def delete(request, id):
    id_organisateur = User.objects.get(id=id)
    myVar = Event.objects.get(id=id)
    myVar.delete()
    return render(request ,'events/index.html')

def edit(request, id):
    event = Event.objects.get(id=id)
    form = EventForm(instance = event)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect("index")  
    return render(request, "events/show_edit.html", context={'event':event})
    

    
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



class SearchResultsView(ListView):
        model = Event
        template_name = 'events/search_results.html'
    
        def get_queryset(self): 
            query = self.request.GET.get("q")
            object_list = Event.objects.filter(
            Q(name=query) | Q(lieu=query)
                )
            return object_list
class HomePageView(TemplateView):
    template_name = 'events/index.html'




def subscribe(request):
     if request.method == "POST":
        email = request.POST.get('email')
        if not email:
          messages="Entrez l'email"
          return render(request, 'events/index.html')
        if email:
          subscribe_user = SubscribedUsers.objects.filter(email=email).first()
          if subscribe_user:
              messages="Email exist deja"
              return render(request, 'events/index.html')
          else:
                elmt = SubscribedUsers.object.create(email=email)
                elmt.save()
        return redirect("home")
     

@login_required
def newsletter(request):
    form = NewsletterForm(request.POST)
    if request.method == "POST":
        subject = request.POST.get('subject')
        message_contenu = request.POST.get('description')
        from_email = settings.EMAIL_HOST_USER
        recipient_list = SubscribedUsers.objects.all()
        mail = EmailMessage(subject, message_contenu, from_email, [recipient_list])
        mail.send() 
        return render(request, 'events/confirmation.html') 