
from django.shortcuts import render
import re
from django.utils.timezone import datetime 

from django.shortcuts import redirect
from reservation_room.forms import LogMessageForm
from reservation_room.models import LogMessage
from reservation_room.models import client
import pyodbc
import os


# Create your views here.
"""def reservation_room(request):
    return render(request, "reservation_room/reservation_room.html")"""


def reservation_room_there(request, name):
    return render(
        request,
        'reservation_room/reservation_room_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def reservation_vol(request):
    return render(request, "reservation_room/reservation_vol.html")

def contact(request):
    return render(request, "reservation_room/contact.html")

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "reservation_room/log_message.html", {"form": form})

def reservation_room(request):     
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                            'SERVER=FC411-25;'
                            'DATABASE=reservationbdd;'
                            'USER=sa;'
                            'PASSWORD=secret;')
    #conn = pyodbc.connect("DRIVER={SQL Server},SERVER="+Server+",DATABASE="+Database+",USER="+UserId+",Authentication=ActiveDirectoryInteractive,Encrypt=yes,PASSWORD="+Password)
    #conn = pyodbc.connect("DRIVER={SQL Server};SERVER="+os.environ.get("DB_SERVER")+";DATABASE="+os.environ.get("DB_NAME")+";USER="+os.environ.get("DB_USER")+";Authentication=ActiveDirectoryInteractive;Encrypt=yes;PASSWORD="+ os.environ.get("DB_PASSWORD"))
    #conn = pyodbc.connect("DRIVER={SQL Server};SERVER=FC411-25;DATABASE=reservationbdd;USER=sa;PASSWORD=secret")

    if request.method == "POST":
        if  request.POST.get('nom') and   request.POST.get('prenom') and +\
            request.POST.get('adresse') and   request.POST.get('telephone') and  +\
            request.POST.get('email') and   request.POST.get('datenaissance') and  +\
            request.POST.get('numeropasseport'):
            insertstValues=client()
            insertstValues.nom = request.POST.get('nom')
            insertstValues.prenom  =request.POST.get('prenom')
            insertstValues.adresse =request.POST.get('adresse')
            insertstValues.telephone =request.POST.get('telephone')
            insertstValues.email =request.POST.get('email')
            insertstValues.dateNaissance =request.POST.get('datenaissance')
            insertstValues.numero_passport =request.POST.get('numeropasseport') 
            cursor=conn.cursor() 
            cursor.execute("INSERT INTO Client VALUES ('"+ insertstValues.nom+"','"+ insertstValues.prenom+"','"+ insertstValues.adresse+"','"+ insertstValues.telephone+"','"+ insertstValues.email+"','"+ insertstValues.dateNaissance+"','"+ insertstValues.numero_passport+"') ")
            cursor.commit()
            return render(request, reservation_room.html)
    else:
        return  render(request, reservation_room.html)
            







