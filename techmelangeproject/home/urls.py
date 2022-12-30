from django.contrib import admin
from django.urls import path
from home import views

#for images
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< HEAD
    path("sponsers/",views.sponsers,name="sponsers"),
    path("event/event_id=<event_id>",views.event,name='event'),
=======
    path("sponsers/",views.sponsers, name='Sponsers'),
    path("event/event_id=<event_id>",views.event,name='event'),
    #for images
    # path('admin/',admin.site.urls),
    # path('', include ('b.urls')),
>>>>>>> 92e33cf4995f2c6bf555dca59557769aac4702bb
]

#for images
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA URL, document_root=settings.MEDIA_ROOT)
