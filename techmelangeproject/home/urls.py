from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('', views.home, name='home'),
    path("Hardcode/",views.Hardcode, name='Hardcode'),
    path("design/",views.design , name='Design-o-web'),
    path("Lan/",views.Lan, name='Lan-o-mania'),
    path("hackathon/",views.hackathon, name='Hackathon'),
    path("Whizquiz/",views.Whizquiz, name='Whizquiz'),
    path("Techcharades/",views.Techcharades, name='Techcharades'),
    path("sponsers/",views.sponsers, name='Sponsers'),
]
