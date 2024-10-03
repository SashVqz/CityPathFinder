import random

def calculateTotalDistance(graph, path):
    """Calculate the total distance of a given path."""
    totalDistance = 0
    for i in range(len(path) - 1):
        totalDistance += graph.edges[path[i]][path[i + 1]]
    # Return to the start
    totalDistance += graph.edges[path[-1]][path[0]]
    return totalDistance

def createInitialPopulation(graph, population_size):
    """Create an initial population of random paths."""
    population = []
    nodes = list(range(len(graph.edges)))
    for _ in range(population_size):
        path = nodes[:]
        random.shuffle(path)
        population.append(path)
    return population

def selectParents(population, graph):
    """Select two parents from the population using tournament selection."""
    tournament_size = 5
    tournament = random.sample(population, tournament_size)
    tournament.sort(key=lambda path: calculateTotalDistance(graph, path))
    return tournament[0], tournament[1]

def crossover(parent1, parent2):
    """Perform ordered crossover (OX) on two parents to create a child."""
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start:end] = parent1[start:end]
    pointer = end
    for node in parent2:
        if node not in child:
            if pointer >= size:
                pointer = 0
            child[pointer] = node
            pointer += 1
    return child

def mutate(path, mutation_rate):
    """Perform swap mutation on a path."""
    for i in range(len(path)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(path) - 1)
            path[i], path[j] = path[j], path[i]

def geneticAlgorithm(graph, population_size, generations, mutation_rate):
    """Optimize a path using a genetic algorithm."""
    population = createInitialPopulation(graph, population_size)
    best_path = min(population, key=lambda path: calculateTotalDistance(graph, path))
    best_distance = calculateTotalDistance(graph, best_path)

    for _ in range(generations):
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = selectParents(population, graph)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = new_population
        current_best_path = min(population, key=lambda path: calculateTotalDistance(graph, path))
        current_best_distance = calculateTotalDistance(graph, current_best_path)
        if current_best_distance < best_distance:
            best_path = current_best_path
            best_distance = current_best_distance

    return best_path, best_distance