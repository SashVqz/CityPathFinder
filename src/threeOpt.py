def calculateTotalDistance(graph, path):
    """Calculate the total distance of a given path."""
    totalDistance = 0
    for i in range(len(path) - 1):
        totalDistance += graph.edges[path[i]][path[i + 1]]
    # Return to the start
    totalDistance += graph.edges[path[-1]][path[0]]
    return totalDistance

def threeOpt(graph, path):
    """
    Optimize a given path using the 3-Opt algorithm.
    The 3-Opt algorithm is a local search algorithm for solving the 
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
    def generate_permutations(path, i, j, k):
        """Generate all permutations of the path by reversing segments."""
        new_paths = []
        new_paths.append(path[:i] + path[i:j][::-1] + path[j:k][::-1] + path[k:])
        new_paths.append(path[:i] + path[i:j][::-1] + path[j:k] + path[k:])
        new_paths.append(path[:i] + path[i:j] + path[j:k][::-1] + path[k:])
        new_paths.append(path[:i] + path[i:j] + path[j:k] + path[k:])
        new_paths.append(path[:i] + path[j:k] + path[i:j] + path[k:])
        new_paths.append(path[:i] + path[j:k][::-1] + path[i:j][::-1] + path[k:])
        return new_paths

    bestPath = path
    bestDistance = calculateTotalDistance(graph, bestPath)
    improved = True

    while improved:
        improved = False
        for i in range(len(bestPath) - 2):
            for j in range(i + 1, len(bestPath) - 1):
                for k in range(j + 1, len(bestPath)):
                    for newPath in generate_permutations(bestPath, i, j, k):
                        newDistance = calculateTotalDistance(graph, newPath)
                        if newDistance < bestDistance:
                            bestPath = newPath
                            bestDistance = newDistance
                            improved = True

    return bestPath, bestDistance