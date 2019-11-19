from django.urls import path
from . import views

app_name = "rooms"

# path(url, funtion, name ... )
# path have integer named 'pk'
# and path find pk argument in ftn
urlpatterns = [
    path("<int:pk>", views.room_detail, name="detail"),
]
