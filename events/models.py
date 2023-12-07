from django.db import models
from django.utils import timezone
from django.urls import reverse


class Event(models.Model):
    name= models.CharField(max_length=128)
    lieu = models.CharField(max_length=128)
    
    event_date = models.DateTimeField()
   
    nbr_ticket = models.IntegerField(default=0)
    # starred = models.BooleanField(default=False)
    slug = models.SlugField(max_length=128)

    def __str__(self):
        return self.name


class Recevoir(models.Model):
    qte = models.IntegerField()
    email = models.EmailField()


# class Organisateur(models.Model):
#     name = models.CharField(max_length=128)
#     email = models.EmailField()
#     password = 
