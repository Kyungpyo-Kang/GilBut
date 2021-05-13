from django.shortcuts import render, redirect
from .models import Node
import random

def home(request):
    return render(request, 'index.html')


def makeNode(request):
    
    
    '''
    nodeID = models.IntegerField(primary_key=True)
    nodeType = models.IntegerField()
    nodeLat = models.CharField(max_length=15)
    nodeLng = models.CharField(max_length=15)
    '''
    initLat = 37.5727506
    initLng = 126.9632605
    originLng = initLng
    indent = 0.00005
    seq = 1
    for i in range(10):
        
        for j in range(10):
            initLat = round(initLat, 10)
            initLng = round(initLng, 10)
            node = Node()
            node.nodeID = seq

            rand = random.randint(1,101)
            nodeType = 0
            if rand >= 30:
                nodeType = 1
            nodeLat = str(initLat)
            nodeLng = str(initLng)
            node.nodeType = nodeType
            node.nodeLat = nodeLat
            node.nodeLng = nodeLng

            node.save()

            initLng += indent
            seq += 1
            print(seq)
        
        initLat -= indent
        initLng = originLng

    
    return redirect('index')

def selectNodes(request):
    nodes = Node.objects
    return render(request, 'viewNode.html', {'nodes':nodes})

def jpsSearch(request):
    return render(request, 'jpsSearch.html')

def jpsResult(request):
    startNode = Node.objects.filter(nodeID=int(request.GET['startNode']))[0]
    endNode = Node.objects.filter(nodeID=int(request.GET['endNode']))[0]
    print(startNode)
    print(endNode)
    results = [startNode, endNode]
    return render(request, 'jpsResult.html', {'results':results})
    




