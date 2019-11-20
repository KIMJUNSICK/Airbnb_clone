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
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    instant = request.GET.get("instant")
    superhost = request.GET.get("superhost")
    selected_amenities = request.GET.getlist("amenities")
    selected_facilities = request.GET.getlist("facilities")

    form = {
        "city": city,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "instant": instant,
        "superhost": superhost,
        "selected_country": country,
        "selected_room_type": room_type,
        "selected_amenities": selected_amenities,
        "selected_facilities": selected_facilities,
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
