
#  main.py
#  RRT Algorithm
#
#  Created by David Khachatryan on 9/17/24.
#
import numpy as np
import matplotlib.pyplot as plt

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
    run_mpl(xpoints, ypoints)

def setup_mpl():
    ########## Begin_Citation [1] ##########
    ax = plt.gca()
    ax.set_xlim([0, 100])
    ax.set_ylim([0, 100])
    ########## End_Citation [1] ##########

def run_mpl(xpoints, ypoints):
    plt.plot(xpoints, ypoints, 'o', markersize=1)
    plt.savefig('linear.pdf')

if __name__ == "__main__":
    main()