from django.shortcuts import render, redirect
from .models import GridMap

import random

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
                print(current)
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def home(request):
    return render(request, 'index.html')


def makeGridMap(request):
    
    initLat = 37.5727506
    initLng = 126.9632605
    originLng = initLng
    indent = 0.00005
    seq = 1
    for i in range(10):
        
        for j in range(10):
            initLat = round(initLat, 10)
            initLng = round(initLng, 10)
            grid = GridMap()
            grid.gridID = seq

            rand = random.randint(1,101)
            gridType = 0
            '''
            if 30 <= rand < 60:
                gridType = 1
            elif 60 <= rand <101:
                gridType= 2 
            '''
            if rand > 70:
                gridType = 1
            gridLat = str(initLat)
            gridLng = str(initLng)
            grid.gridType = gridType
            grid.gridLat = gridLat
            grid.gridLng = gridLng
            grid.gridRow = i
            grid.gridCol = j
            
            grid.save()
            
            initLng += indent
            seq += 1
            
        
        initLat -= indent
        initLng = originLng

    
    return redirect('index')

def selectMap(request):
    grids = GridMap.objects
    return render(request, 'viewNode.html', {'grids':grids})

def jpsSearch(request):
    return render(request, 'jpsSearch.html')

def jpsResult(request):
    
    grids = GridMap.objects
    map = []
    content = []
    for grid in grids.all():
        if grid.gridID%10 == 0:
            content.append(grid.gridType)
            map.append(content)
            content = []
        else:
            content.append(grid.gridType)
    
    startNode = GridMap.objects.filter(gridID=int(request.GET['startNode']))[0]
    endNode = GridMap.objects.filter(gridID=int(request.GET['endNode']))[0]
    
    start = (startNode.gridRow, startNode.gridCol)
    end = (endNode.gridRow, endNode.gridCol)
    
    
    path = astar(map, start, end)
    
    
    return render(request, 'jpsResult.html', {'results':path, 'map':map})
    




