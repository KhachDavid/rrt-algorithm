
#  main.py
#  RRT Algorithm
#
#  Created by David Khachatryan on 9/17/24.
#
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import sys

from modules.Graph import Graph
from modules.Obstacle import Obstacle

# GRAPH SIZE
graph_startx = 0
graph_starty = 0
graph_endx = 1000
graph_endy = 1000

# START and END goal
startx=20
starty=0
endx=900
endy=900

K = sys.maxsize

def main():

    # Initialize G with q_init
    graph = Graph(start_x=startx, start_y=starty, end_x=endx, end_y=endy, start_dx=graph_startx, start_dy=graph_starty, end_dx=graph_endy, end_dy=graph_endy)

    for i in range(K):
        q_rand = graph.random_configuration()
        nearest_vertex = graph.nearest_vertex(q_rand)
        new_node = graph.new_configuration(nearest_vertex, q_rand)

        # Check if the new node collides with any obstacles
        collision = False
        for o in graph.obstacles:
            if o.is_inside(new_node.x, new_node.y):
                collision = True
                break 
        
        # Do not add this vertex if there is collision
        if collision:
            continue

        graph.add_vertex(new_node)
        graph.add_edge(new_node, nearest_vertex)

        if not graph.check_line_collision((new_node.x, new_node.y), (graph.end_x, graph.end_y)):
            print(f"Found the path on iteration: {i}")
            start_point = (new_node.x, new_node.y)
            goal_point = (graph.end_x, graph.end_y) 
            xpoints, ypoints = graph.get_points()
            setup_mpl()
            run_mpl(xpoints, ypoints, graph.edges, graph.obstacles, start_point, goal_point, startx, starty)

            break


def setup_mpl():
    ########## Begin_Citation [1] ##########
    ax = plt.gca()
    ax.set_xlim([graph_startx, graph_endx])
    ax.set_ylim([graph_starty, graph_endy])
    ########## End_Citation [1] ##########

def run_mpl(xpoints, ypoints, edges, obstacles: list, start: tuple, goal: tuple, start_dx, start_dy):
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
    ax.plot(start_dx, start_dy, 'o', color='cyan', markersize=4, label='Start')  # Adjust size as needed
    # Create a LineCollection from the edges
    line_segments = LineCollection(formatted_edges, linewidths=1)
    
    # Add the line collection to the axis
    ax.add_collection(line_segments)
    
    # Plot circles for obstacles
    for o in obstacles:
        circle = plt.Circle((o.cX, o.cY), o.radius, color='blue', fill=True)
        ax.add_artist(circle)

    # Optionally, plot the start and goal points
    ax.plot(start[0], start[1], 'go', markersize=5, label='Final Vector')  # Green circle for the start
    ax.plot(goal[0], goal[1], 'ro', markersize=5, label='Goal')  # Red circle for the goal

    # Plot the straight line from the start to the goal
    ax.plot([start[0], goal[0]], [start[1], goal[1]], 'r--', label='Collision-free path')  # Red dashed line for the path
    ax.autoscale()
    
    # Add legend
    ax.legend()
    
    plt.savefig('linear.pdf')

    ########## End_Citation [3] ##########

if __name__ == "__main__":
    main()