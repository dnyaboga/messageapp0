from django.contrib import admin
from .models import *

admin.site.register(BreastScreening)
admin.site.register(BreastResult)
admin.site.register(CervicalScreening)
admin.site.register(CervicalResult)
admin.site.register(NotifyBreast)
admin.site.register(NotifyCervical)
admin.site.register(Person)
admin.site.register(Contact)
admin.site.register(EncounterType)
admin.site.register(Patient)