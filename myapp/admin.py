from django.contrib import admin
from .models import Location
from.models import Asiento
from.models import Reserva

# Register your models here.
admin.site.register(Location)
admin.site.register(Asiento)
admin.site.register(Reserva)