from django.contrib import admin
from django.urls import path
import MapAPI.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MapAPI.views.home, name='index'),
    path('makeGridMap', MapAPI.views.makeGridMap, name='makeGridMap'),
    path('selectMap', MapAPI.views.selectMap, name='selectMap'),
    path('jpsSearch', MapAPI.views.jpsSearch, name='jpsSearch'),
    path('jpsResult', MapAPI.views.jpsResult, name='jpsResult'),
]
