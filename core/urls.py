from django.urls import path
from rooms import views as room_views

app_name = "core"

# path(url, funtion, name ... )
# HomeView is not function, class
urlpatterns = [
    path("", room_views.HomeView.as_view(), name="home"),
]
