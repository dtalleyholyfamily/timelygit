from django.urls import path
from calendartimely import views

app_name = "calendartimely"
urlpatterns = [
    path("", views.index, name="index"),
    path("calendar/", views.CalendarView.as_view(), name="calendar"),
    path("event/new", views.event, name="event_new"),
    path("event/edit(<event_id>)", views.event, name="event_edit"),
]