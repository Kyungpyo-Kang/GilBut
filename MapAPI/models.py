from django.db import models

class Node(models.Model):
    nodeID = models.IntegerField(primary_key=True)
    nodeType = models.IntegerField()
    nodeLat = models.CharField(max_length=15)
    nodeLng = models.CharField(max_length=15)

    def __str__(self):
        return str(self.nodeID)

