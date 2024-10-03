class Graph:
    """
    Graph class represents a graph data structure with nodes and edges.
    Attributes:
        nodes (dict): A dictionary where keys are node IDs and values are tuples containing node name, latitude, and longitude.
        edges (dict): A dictionary where keys are node IDs and values are dictionaries representing edges and their distances.
    Methods:
        __init__():
            Initializes an empty graph with nodes and edges.
        
        addNode(nodeId, name, latitude, longitude):
            Adds a node to the graph.
            Parameters:
                nodeId (int): Unique identifier for the node.
                name (str): Name of the node.
                latitude (float): Latitude of the node.
                longitude (float): Longitude of the node.
        
        addEdge(fromNode, toNode, distance):
            Adds an undirected edge between two nodes in the graph.
            Parameters:
                fromNode (int): The starting node ID.
                toNode (int): The ending node ID.
                distance (float): The distance between the nodes.
    """
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def addNode(self, nodeId, name, latitude, longitude):
        self.nodes[nodeId] = (name, latitude, longitude)
        self.edges[nodeId] = {}

    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode][toNode] = distance
        self.edges[toNode][fromNode] = distance  # Undirected graph