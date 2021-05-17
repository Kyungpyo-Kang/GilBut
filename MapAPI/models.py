from django.db import models

class GridMap(models.Model):
    gridID = models.IntegerField(primary_key=True)
    gridType = models.IntegerField()
    gridLat = models.CharField(max_length=15)
    gridLng = models.CharField(max_length=15)
    gridRow = models.IntegerField()
    gridCol = models.IntegerField()
    