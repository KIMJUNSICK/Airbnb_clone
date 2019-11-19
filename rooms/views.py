from django.views.generic import ListView, DetailView
from django.shortcuts import render
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
    city = str.capitalize(request.GET.get("city"))  # Start with a capital letter in DB
    return render(request, "rooms/search.html", {"city": city})
