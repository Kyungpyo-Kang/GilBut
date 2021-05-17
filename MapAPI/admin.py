from django.contrib import admin
from MapAPI.models import GridMap

# Register your models here.

class GridMapAdmin(admin.ModelAdmin):
    list_display = ('gridID', 'gridType', 'gridLat', 'gridLng')

admin.site.register(GridMap, GridMapAdmin)