from django.contrib import admin
from home.models import Registration
from home.models import festdesc
from home.models import sponsers, teachcoor
# Register your models here.
admin.site.register(Registration)
admin.site.register(festdesc)
admin.site.register(sponsers)
admin.site.register(teachcoor)


