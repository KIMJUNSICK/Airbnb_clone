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
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
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
    selected_house_rules = request.GET.getlist("house_rules")

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
        "selected_house_rules": selected_house_rules,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()
    house_rules = models.HouseRule.objects.all()
    choices = {
        "room_types": room_types,
        "countries": countries,
        "amenities": amenities,
        "facilities": facilities,
        "house_rules": house_rules,
    }

    filter_args = {}

    # filtering
    if city != "Anywhere":
        filter_args["city__startswith"] = city
    if room_type != 0:
        filter_args["room_type__pk"] = room_type
    filter_args["country"] = country

    rooms = models.Room.objects.filter(**filter_args)

    print(filter_args)
    print(rooms)

    # filter rooms in db by data that get in url
    # get data of rooms that were filtered
    # send the data to templates
    # view + css

    return render(request, "rooms/search.html", {**form, **choices, "rooms": rooms})

