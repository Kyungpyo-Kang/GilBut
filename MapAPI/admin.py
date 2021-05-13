from django.contrib import admin
from MapAPI.models import Node

# Register your models here.

class NodeAdmin(admin.ModelAdmin):
    list_display = ('nodeID', 'nodeType', 'nodeLat', 'nodeLng')

admin.site.register(Node, NodeAdmin)