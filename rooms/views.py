from django.views.generic import ListView, DetailView
from django.shortcuts import render
from . import models, forms


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
    country = request.GET.get("country")

    if country:
        form = forms.SearchForm(
            request.GET
        )  # bounded form # connected to data, automatically check data

        if form.is_valid():
            print(form.cleaned_data)  # get cleaned data in request of ours

    else:
        form = forms.SearchForm()  # undounded form # set default value

    return render(request, "rooms/search.html", {"form": form})

