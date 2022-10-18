from django.db import models 
from django.utils import timezone

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField()



    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"




class reservation_room(models.Model): 
    reservationId = models.AutoField(primary_key=True)
    nom_chambre = models.CharField(max_length=150) 
    Checkin  = models.DateTimeField()
    Checkout  = models.DateTimeField()
    nb_adultes = models.IntegerField()
    nb_enfants = models.IntegerField()
    clientId  = models.IntegerField()
    
    
class client(models.Model):  
    clientId = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=150) 
    prenom = models.CharField(max_length=150) 
    adresse = models.CharField(max_length=150) 
    telephone = models.CharField(max_length=100) 
    email = models.CharField(max_length=150)
    dateNaissance = models.DateTimeField()
    numero_passport = models.IntegerField()
