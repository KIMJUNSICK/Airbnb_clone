from django.shortcuts import render
from . import models


def all_rooms(request):
    # infomation of page in request
    # how to get page info neatly in queryset
    #  variable for offset & limit
    #  offset = (page-1) x 10 limit = page x 10
    #  all_rooms = models.Room.objects.all()[offset:limit]
    PAGE_SIZE = 10
    page = int(request.GET.get("page", 1))
    limit = page * PAGE_SIZE
    offset = limit - PAGE_SIZE
    all_rooms = models.Room.objects.all()[offset:limit]  # [Offset : Limit]
    return render(request, "rooms/home.html", context={"potato": all_rooms})
