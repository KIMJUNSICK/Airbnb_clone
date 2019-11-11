from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    """ List Admin Definition"""

    # insice
    filter_horizontal = ("rooms",)

    # outside
    list_display = (
        "name",
        "user",
        "count_rooms",
    )

    search_fields = ("name",)
