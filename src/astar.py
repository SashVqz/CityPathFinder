# src/astar.py
import heapq
from utils import haversine, heuristic, reconstructPath


def aStar(graph, startId, goalId):
    """
    Implementation of the A* algorithm to find the shortest path.
    Args:
        graph (Graph): The graph on which to perform the A* search. It should have 'nodes' and 'edges' attributes.
        startId (int): The starting node ID.
        goalId (int): The goal node ID.
    Returns:
        list: The shortest path from startId to goalId as a list of node IDs, or None if no path is found.
    """
    openSet = []
    heapq.heappush(openSet, (0, startId))
    
    cameFrom = {}
    gScore = {node: float('inf') for node in graph.nodes}
    gScore[startId] = 0
    
    fScore = {node: float('inf') for node in graph.nodes}
    fScore[startId] = heuristic(graph.nodes[startId], graph.nodes[goalId])
    
    while openSet:
        current = heapq.heappop(openSet)[1]
        
        if current == goalId:
            return reconstructPath(cameFrom, current)
        
        for neighbor, distance in graph.edges[current]:
            tentativeGScore = gScore[current] + distance
            if tentativeGScore < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = tentativeGScore
                fScore[neighbor] = gScore[neighbor] + heuristic(graph.nodes[neighbor], graph.nodes[goalId])
                heapq.heappush(openSet, (fScore[neighbor], neighbor))
    
    return None

