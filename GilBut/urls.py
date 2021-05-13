from django.contrib import admin
from django.urls import path
import MapAPI.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MapAPI.views.home, name='index'),
    path('makeNode', MapAPI.views.makeNode, name='makeNode'),
    path('selectNodes', MapAPI.views.selectNodes, name='selectNodes'),
    path('jpsSearch', MapAPI.views.jpsSearch, name='jpsSearch'),
    path('jpsResult', MapAPI.views.jpsResult, name='jpsResult'),
]
