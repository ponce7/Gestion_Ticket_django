from django.db import models
from django.utils import timezone
from django.urls import reverse
from EvenementProject.settings import AUTH_USER_MODEL

# Create your models here.
# class Event(models.Model):
#     name = models.CharField(max_length=128)
#     
#     nbr_ticket = models.IntegerField(default=0)
#    
#     slug = models.SlugField(max_length=128)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("event", kwargs={"slug": self.slug})

class Event(models.Model):
    # photo models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    
    name= models.CharField(max_length=128)
    lieu = models.CharField(max_length=128)
    
    event_date = models.DateTimeField(blank=True, null=True)
    nbr_ticket = models.IntegerField(default=0)
    # starred = models.BooleanField(default=False)
    slug = models.SlugField(max_length=128)

    def __str__(self):
        return self.name


class Recevoir(models.Model):
    elem = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True)
    qte = models.IntegerField()
    email = models.EmailField()

# class Utilisateur(models.Model):
#     email = models.EmailField()
    


class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.event.name} ({self.quantity})"


class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):  
        return self.user.email

    def delete(self, *args, **kwargs):
        for order in self.orders.all():
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()

        self.orders.clear()
        super().delete(*args, **kwargs)
