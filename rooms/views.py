from django.shortcuts import render
from . import models
from math import ceil


def all_rooms(request):
    PAGE_SIZE = 10
    page = request.GET.get("page", 1)
    page = int(page or 1)  # for case that there are imcomplete page
    limit = page * PAGE_SIZE
    offset = limit - PAGE_SIZE
    page_count = ceil(models.Room.objects.count() / PAGE_SIZE)
    all_rooms = models.Room.objects.all()[offset:limit]  # [Offset : Limit]
    return render(
        request,
        "rooms/home.html",
        context={
            "potato": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count + 1),
            "page_previous": page - 1,
            "page_next": page + 1,
        },
    )
