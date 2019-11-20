from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from . import models


# abstract because of reusing this in another views
class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ RoomDetail Definition"""

    model = models.Room


def search(request):
    city = str.capitalize(
        request.GET.get("city", "Anywhere")  # default
    )  # Start with a capital letter in DB
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    form = {
        "city": city,
        "selected_country": country,
        "selected_room_type": room_type,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()
    choices = {
        "room_types": room_types,
        "countries": countries,
        "amenities": amenities,
        "facilities": facilities,
    }

    return render(request, "rooms/search.html", {**form, **choices})
