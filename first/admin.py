from django.contrib.gis import admin
from models import First

admin.site.register(First, admin.GeoModelAdmin)
