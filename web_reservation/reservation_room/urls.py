from django.urls import path
from . import views

urlpatterns = [
    path("", views.reservation_room, name="reservation_room"),
    path("reservation_room_there/<name>", views.reservation_room_there, name="reservation_room_there"),
    path("reservation_vol/", views.reservation_vol, name="reservation_vol"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"), 
]