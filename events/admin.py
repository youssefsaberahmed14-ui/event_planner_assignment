from django.contrib import admin
from .models import Event

# سجل الموديل عشان يظهر في Admin
admin.site.register(Event)
