from django.contrib import admin

from .models import Prestamo
from .models import Estado

admin.site.register(Prestamo)
admin.site.register(Estado)
# Register your models here.
