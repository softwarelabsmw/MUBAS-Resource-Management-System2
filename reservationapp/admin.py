############ PYTHON FILE FOR REGISTERING DB TABLES IN THE DJANGO ADMINISTRATION PANEL #########################################

from django.contrib import admin

from .models import (Resource, Booking)

admin.site.register(Resource)
admin.site.register(Booking)

