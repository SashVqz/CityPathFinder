# src/tsp.py
def nearestNeighborTsp(graph, startNode):
    """
    Finds an approximate solution to the Traveling Salesman Problem (TSP) using the nearest neighbor heuristic.
    Parameters:
    graph (Graph): A graph object where `graph.nodes` is a list of nodes and `graph.edges` is a dictionary 
                   where keys are node indices and values are dictionaries of neighboring node indices and 
                   their corresponding edge weights.
    startNode (int): The index of the starting node for the TSP.
    Returns:
    tuple: A tuple containing:
        - path (list): A list of node indices representing the order in which nodes are visited in the TSP path.
        - totalDistance (float): The total distance of the TSP path.
    """
    numNodes = len(graph.nodes)
    visited = [False] * numNodes
    path = [startNode]
    visited[startNode] = True
    currentNode = startNode
    totalDistance = 0
    
    for _ in range(numNodes - 1):
        nearestNode = None
        nearestDistance = float('inf')
        
        for neighbor, distance in graph.edges[currentNode].items():
            if not visited[neighbor] and distance < nearestDistance:
                nearestNode = neighbor
                nearestDistance = distance
        
        if nearestNode is not None:
            path.append(nearestNode)
            visited[nearestNode] = True
            totalDistance += nearestDistance
            currentNode = nearestNode

    # Return to the starting point to close the cycle
    totalDistance += graph.edges[currentNode][startNode]
    path.append(startNode)
    
    return path, totalDistance
