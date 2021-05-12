from django.contrib import admin
from django.urls import path
import MapAPI.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MapAPI.views.home, name='home/'),
]
