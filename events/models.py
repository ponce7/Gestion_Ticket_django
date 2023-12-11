from django.db import models
from django.utils import timezone
from django.urls import reverse

from io import BytesIO

from barcode import EAN13
from PIL import Image, ImageDraw
from django.core.files import File
import qrcode 

class Event(models.Model):
    name= models.CharField(max_length=128)
    lieu = models.CharField(max_length=128)
    event_date = models.DateTimeField()
    event_photo = models.ImageField(upload_to="image/")
    nbr_ticket = models.IntegerField(default=0)
    slug = models.SlugField(max_length=128)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    qr_code = models.ImageField(upload_to="image/")
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

class Recevoir(models.Model):
    qte = models.IntegerField()
    email = models.EmailField()


# class Organisateur(models.Model):
#     name = models.CharField(max_length=128)
#     email = models.EmailField()
#     password = 
