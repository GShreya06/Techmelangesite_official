from django.contrib import admin
from django.urls import path
from home import views

#for images
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path("sponsers/",views.sponsers, name='Sponsers'),
    path("event/event_id=<event_id>",views.event,name='event'),
]

#for images
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA URL, document_root=settings.MEDIA_ROOT)
