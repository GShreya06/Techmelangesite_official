from django.contrib import admin
from home.models import Registration
from home.models import festdesc
<<<<<<< HEAD
from home.models import sponsers, teachcoor
# Register your models here.
admin.site.register(Registration)
admin.site.register(festdesc)
admin.site.register(sponsers)
admin.site.register(teachcoor)


=======
from home.models import *
# Register your models here.
admin.site.register(Registration)
admin.site.register(festdesc)
admin.site.register(events)
>>>>>>> 2f92d2b76ed3506dc36c32c465d91f92bbe09d05
