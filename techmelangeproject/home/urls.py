from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('', views.home, name='home'),
    path("sponsers/",views.sponsers,name="sponsers"),
    path("event/event_id=<event_id>",views.event,name='event'),
]
