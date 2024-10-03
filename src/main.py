# src/main.py
"""
This script performs the following tasks:
1. Loads a city graph from a CSV file.
2. Defines a start node for the Traveling Salesman Problem (TSP).
3. Solves the TSP using the nearest neighbor algorithm.
4. Optimizes the initial TSP route using the 2-Opt algorithm.
5. Prints the optimized route and total distance.
6. Generates a Google Maps URL to visualize the optimized route.
Modules:
- pandas: Used for data manipulation and CSV handling.
- loader: Contains the function `loadDataFromCsv` to load the city graph.
- tsp: Contains the function `nearestNeighborTsp` to solve the TSP.
- twoOpt: Contains the function `twoOpt` to optimize the TSP route.
- utils: Contains utility functions `createGoogleMapsUrl` and `getCoordinatesFromPath`.
Functions:
- loadDataFromCsv(filePath): Loads the city graph from a CSV file.
- nearestNeighborTsp(graph, startNode): Solves the TSP using the nearest neighbor algorithm.
- twoOpt(graph, path): Optimizes the TSP route using the 2-Opt algorithm.
- createGoogleMapsUrl(coordinates): Generates a Google Maps URL for the given coordinates.
- getCoordinatesFromPath(graph, path): Retrieves the coordinates for the given path.
Usage:
Run this script as the main module to execute the TSP solution and optimization process.
"""
import pandas as pd
import time
from loader import loadDataFromCsv
from tsp import nearestNeighborTsp
from twoOpt import twoOpt
from utils import createGoogleMapsUrl, getCoordinatesFromPath, getCoordinates

if __name__ == '__main__':
    # # Read place names from the text file
    # with open('routes/seattle.txt', 'r') as file:  # Change to your text file name
    #     places = [line.strip() for line in file.readlines()]

    # # List to store the data
    # data = []

    # for idx, place in enumerate(places, start=1):
    #     latitude, longitude = getCoordinates(place)
    #     if latitude is not None and longitude is not None:
    #         data.append([idx, place, latitude, longitude])
    #     else:
    #         print(f"Could not find coordinates for: {place}")
    #     time.sleep(1)  # Pause to avoid exceeding the request limit

    # # Create a DataFrame and save as CSV
    # df = pd.DataFrame(data, columns=['id', 'name', 'latitude', 'longitude'])
    # df.to_csv('data/locations.csv', index=False)  # Change to your desired CSV file name
    # print("CSV successfully generated: data/locations.csv")

    # Load the city graph
    graph = loadDataFromCsv('data/seattle.csv')  # Change to your CSV file name
    
    # Define the start node (can be any point, e.g., Space Needle)
    startNode = 1  # Space Needle
    
    # Solve the TSP using the nearest neighbor algorithm
    initialPath, _ = nearestNeighborTsp(graph, startNode)
    
    # Optimize the route with 2-Opt
    optimizedPath, totalDistance = twoOpt(graph, initialPath)
    
    print(f'Optimized route (2-Opt): {optimizedPath}')
    print(f'Total optimized distance: {totalDistance:.2f} km')
    
    # Get the coordinates of the optimized route
    coordinates = getCoordinatesFromPath(graph, optimizedPath)
    
    # Generate the Google Maps link
    googleMapsUrl = createGoogleMapsUrl(coordinates)
    print(f'View the optimized route on Google Maps: {googleMapsUrl}')
