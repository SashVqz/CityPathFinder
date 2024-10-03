# src/utils.py
import math
import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim
import time

def heuristic(node1, node2):
    """We use the Haversine distance as a heuristic."""
    _, lat1, lon1 = node1
    _, lat2, lon2 = node2
    return haversine((lat1, lon1), (lat2, lon2))

def haversine(lat1, lon1, lat2, lon2):
    """Calculates the distance between two points using the Haversine formula."""
    R = 6371  # Radius of the Earth in km
    dLat = np.radians(lat2 - lat1)
    dLon = np.radians(lon2 - lon1)
    a = np.sin(dLat / 2) ** 2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dLon / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return R * c

def createGoogleMapsUrl(coordinates):
    """
    Generates a Google Maps URL to visualize a driving route with the given coordinates.
    Args:
        coordinates (list of tuple): A list of tuples where each tuple contains the latitude and longitude of a point.
    Returns:
        str: A URL string that can be used to visualize the route in Google Maps.
    """
    baseUrl = "https://www.google.com/maps/dir/?api=1&travelmode=driving"
    waypoints = ""
    
    for i, (lat, lon) in enumerate(coordinates):
        if i == 0:
            baseUrl += f"&origin={lat},{lon}"
        elif i == len(coordinates) - 1:
            baseUrl += f"&destination={lat},{lon}"
        else:
            waypoints += f"{lat},{lon}|"
    
    if waypoints:
        baseUrl += f"&waypoints={waypoints[:-1]}"
    
    return baseUrl

def getCoordinatesFromPath(graph, path):
    """Gets the coordinates (lat, lon) of the nodes in the path."""
    coordinates = []
    for nodeId in path:
        name, lat, lon = graph.nodes[nodeId]
        coordinates.append((lat, lon))
    return coordinates

def getCoordinates(location):
    geolocator = Nominatim(user_agent="geoapiExercises")
    locationData = geolocator.geocode(location)
    if locationData:
        return locationData.latitude, locationData.longitude
    else:
        return None, None

def reconstructPath(cameFrom, current):
    totalPath = [current]
    while current in cameFrom:
        current = cameFrom[current]
        totalPath.append(current)
    return totalPath[::-1]