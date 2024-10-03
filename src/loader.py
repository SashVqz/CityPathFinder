# src/loader.py
import csv
import numpy as np

from graph import Graph
from utils import haversine

def loadDataFromCsv(filename):
    """
    Load data from a CSV file and create a graph.
    Args:
        filename (str): The path to the CSV file containing the data.
    Returns:
        Graph: A graph object with nodes and edges created from the CSV data.
    The CSV file should have the following columns:
        - id: An integer representing the node ID.
        - name: A string representing the name of the node.
        - latitude: A float representing the latitude of the node.
        - longitude: A float representing the longitude of the node.
    The function performs the following steps:
        1. Reads the CSV file and creates nodes in the graph.
        2. Calculates the distances between all nodes using the Haversine formula.
        3. Adds edges between nodes with the calculated distances.
    """
    graph = Graph()
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            nodeId = int(row['id'])
            name = row['name']
            latitude = float(row['latitude'])
            longitude = float(row['longitude'])
            graph.addNode(nodeId, name, latitude, longitude)

    # Calculate distances between all points
    for nodeId1 in graph.nodes:
        for nodeId2 in graph.nodes:
            if nodeId1 != nodeId2:
                lat1, lon1 = graph.nodes[nodeId1][1:3]
                lat2, lon2 = graph.nodes[nodeId2][1:3]
                distance = haversine(lat1, lon1, lat2, lon2)
                graph.addEdge(nodeId1, nodeId2, distance)

    return graph
