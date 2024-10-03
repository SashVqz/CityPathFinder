def calculateTotalDistance(graph, path):
    """Calculate the total distance of a given path."""
    totalDistance = 0
    for i in range(len(path) - 1):
        totalDistance += graph.edges[path[i]][path[i + 1]]
    # Return to the start
    totalDistance += graph.edges[path[-1]][path[0]]
    return totalDistance

def twoOpt(graph, path):
    """
    Optimize a given path using the 2-Opt algorithm.
    The 2-Opt algorithm is a simple local search algorithm for solving the 
    Traveling Salesman Problem (TSP). It iteratively improves the path by 
    reversing segments of the path to reduce the total distance.
    Args:
        graph (list of list of int): A 2D list representing the adjacency matrix 
            of the graph where graph[i][j] is the distance between node i and node j.
        path (list of int): A list representing the initial path (tour) through the graph.
    Returns:
        tuple: A tuple containing the optimized path (list of int) and the total 
            distance (int) of the optimized path.
    """
    """Optimize the path using the 2-Opt algorithm."""
    bestPath = path
    bestDistance = calculateTotalDistance(graph, bestPath)
    improved = True

    while improved:
        improved = False
        for i in range(1, len(bestPath) - 1):
            for j in range(i + 1, len(bestPath)):
                if j - i == 1:  # Cannot swap adjacent points
                    continue
                # Create a new path
                newPath = bestPath[:]
                newPath[i:j] = reversed(bestPath[i:j])  # Reverse the section
                newDistance = calculateTotalDistance(graph, newPath)

                # If the new distance is better, update the best path
                if newDistance < bestDistance:
                    bestPath = newPath
                    bestDistance = newDistance
                    improved = True

    return bestPath, bestDistance
