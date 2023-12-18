from django.db import models
from django.utils import timezone
from barcode import EAN13



class Event(models.Model):
    name= models.CharField(max_length=128)
    lieu = models.CharField(max_length=128)
    event_date = models.DateTimeField(blank=True, null=True)
    event_photo = models.ImageField(upload_to="image/")
    nbr_ticket = models.IntegerField(default=1)
    price = models.IntegerField()
    id_user = models.IntegerField()
    def __str__(self):
        return self.name
    
   
class Ticket(models.Model):
    qr_code = models.ImageField(upload_to="image/")
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
      
class Recevoir(models.Model):
    qte = models.IntegerField()
    email = models.EmailField()


class Organisateur(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    password = models.CharField(max_length=32)
    eventy = models.ForeignKey('Event', on_delete=models.CASCADE)


class SubscribedUsers(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)


    def __str__(self):
        return self.email


class Newsletter(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=5000)


    def __str__(self):
        return self.subject

