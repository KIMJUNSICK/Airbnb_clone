from django.views.generic import ListView
from . import models


# abstract because of reusing this in another views
class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room

