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
    instant = bool(request.GET.get("instant"))
    superhost = bool(request.GET.get("superhost"))
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
    if price != 0:
        filter_args["price__lte"] = price
    if guests != 0:
        filter_args["guests__gte"] = guests
    if bedrooms != 0:
        filter_args["bedrooms__gte"] = bedrooms
    if beds != 0:
        filter_args["beds__gte"] = beds
    if baths != 0:
        filter_args["baths__gte"] = baths
    if instant is True:
        filter_args["instant_book"] = True
    if superhost is True:
        filter_args["host__superhost"] = True
    filter_args["country"] = country

    rooms = models.Room.objects.filter(**filter_args)

    if len(selected_amenities) > 0:
        for selected_amenity in selected_amenities:
            rooms = rooms & models.Room.objects.filter(
                amenities__pk=int(selected_amenity)
            )
    if len(selected_facilities) > 0:
        for selected_facility in selected_facilities:
            rooms = rooms & models.Room.objects.filter(
                amenities__pk=int(selected_facility)
            )
    if len(selected_house_rules) > 0:
        for selected_house_rule in selected_house_rules:
            rooms = rooms & models.Room.objects.filter(
                amenities__pk=int(selected_house_rule)
            )

    print(selected_amenities)
    print(filter_args)
    print(rooms)

    # filter rooms in db by data that get in url
    # get data of rooms that were filtered
    # send the data to templates
    # view + css

    return render(request, "rooms/search.html", {**form, **choices, "rooms": rooms})

