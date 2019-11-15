from django.shortcuts import render
from datetime import datetime


def all_rooms(request):
    now = datetime.now()
    junsik = True
    return render(request, "all_rooms.html", context={"now": now, "junsik": junsik})
