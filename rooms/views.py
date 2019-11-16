from django.shortcuts import render
from . import models


def all_rooms(request):
    all_rooms = models.Room.objects.all()[3:10]  # [Offset : Limit]
    return render(request, "rooms/home.html", context={"potato": all_rooms})
