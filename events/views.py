from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.urls import reverse
from events.models import Event, Cart, Order
from django.contrib.auth.decorators import login_required
from events.forms import *



from django.core.mail import EmailMessage, get_connection
from django.conf import settings




from django.forms import ModelForm
from .forms import EventForm
# Create your views here.


def index(request):
    events = Event.objects.all()
    return render(request, "events/index.html", context={'events':events})


def add_event(request):  
        if request.method == "POST":
            form = EventForm(request.POST)
            if form.is_valid():
                    form.save()
                    return redirect("index")
            else:
                return render(request, 'events/event.html')
        return render(request, 'events/event.html',{'form':EventForm})     
    

def commande(request, slug):
     events = Event.objects.get(slug=slug)
     if request.method == "POST":
        # if (order.quantity > event.nbr_ticket):
        #         message ="Nombre de ticket en stock insuffisant, commandez en dessous."

        #         return render(request, 'events\index.html', {'message':message})
        # form = RecevoirForm(request.POST)
        # user = request.user
        # event = get_object_or_404(Event, slug=slug)
        # cart, _ = Cart.objects.get_or_create(user=user)
        # order, created = Order.objects.get_or_create(user=user, event=event) 
     
        form = RecevoirForm(request.POST)
        if form.is_valid() :
            
            form.save()
            return redirect('index')
        else:
            return render(request, 'events/commande.html')
        
     return render(request, 'events/commande.html',{'form': RecevoirForm, 'events': events })



def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'events/cart.html', context={"orders": cart.orders.all()})

def send_email(request):
     if request.method == "POST":
          with get_connection(
               host=settings.EMAIL_HOST,
               port=settings.EMAIL_PORT,
               username=settings.EMAIL_HOST_USER,
               password=settings.EMAIL_HOST_PASSWORD,
               use_tls=settings.EMAIL_USE_TLS) as connection:
               subject = request.POST.get("subject")
               email_from = settings.EMAIL_HOST_USER
               recipient_list = [request.POST.get("email")]
               message = request.POST.get("message")
               EmailMessage(subject, message, email_from, recipient_list, connection=connection). send()

               return render(request, 'events/index.html')
          
