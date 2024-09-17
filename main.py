
#  main.py
#  RRT Algorithm
#
#  Created by David Khachatryan on 9/17/24.
#
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

from modules.Graph import Graph
from modules.Node import Node

K = 500


def main():

    # Initialize G with q_init
    graph = Graph(start_x=50, start_y=50, start_dx=0, start_dy=0, end_dx=100, end_dy=100)

    for _ in range(K):
        q_rand = graph.random_configuration()
        nearest_vertex = graph.nearest_vertex(q_rand)
        new_node = graph.new_configuration(nearest_vertex, q_rand)
        graph.add_vertex(new_node)
        graph.add_edge(new_node, nearest_vertex)
    
    xpoints, ypoints = graph.get_points()
    setup_mpl()
    run_mpl(xpoints, ypoints, graph.edges)

def setup_mpl():
    ########## Begin_Citation [1] ##########
    ax = plt.gca()
    ax.set_xlim([0, 100])
    ax.set_ylim([0, 100])
    ########## End_Citation [1] ##########

def run_mpl(xpoints, ypoints, edges):
    ########## Begin_Citation [3] ##########

    # Create a figure and an axis
    fig, ax = plt.subplots()

    # Convert Edge objects into a list of line segments
    formatted_edges = [
        (edge.get_point_one(), edge.get_point_two()) for edge in edges
    ]
    
    # Extract all vertices from the edges (flattened list of points)
    points = [point for edge in formatted_edges for point in edge]
    
    # Separate x and y coordinates of all points
    xpoints, ypoints = zip(*points)
    
    # Plot the vertices as points
    ax.plot(xpoints, ypoints, 'o', markersize=2)
    
    # Create a LineCollection from the edges
    line_segments = LineCollection(formatted_edges, linewidths=1)
    
    # Add the line collection to the axis
    ax.add_collection(line_segments)
    
    # Set limits for the plot
    ax.autoscale()
    plt.savefig('linear.pdf')

    ########## End_Citation [3] ##########


if __name__ == "__main__":
    main()