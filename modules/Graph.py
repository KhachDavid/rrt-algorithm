#
#  Graph.py
#  RRT Algorithm
#
#  Created by David Khachatryan on 9/17/24.
#
import numpy as np
from modules.Node import Node
from modules.Edge import Edge

class Graph:
    """
    Attributes
    ----------
    nodes: Set of vertices represent as Node objects
    edges: Set of x, y pairs that represent Node connectinos as Edge objects
    start_dx: Int for the start of the domain
    start_dy: Int for the start of the domain
    end_dx: Int for the end of the domain
    end_dy: Int for the end of the domain
    delta: Incremental 
    
    Functions
    get_points: Returns two numpy arrays of N length. 
                Array one contains x coordinates
                Array two contains y coordinates
                N = len(self.nodes)

    random_configuration: Returns a random (x, y) in the domain
    nearest_vertex: Takes an argument (x, y). 
                    Returns the nearest vertex in the Graph
    euclidean_distance: Takes two (x, y) arguments
                        Returns euclidean distance between the two
    new_configuration: Takes Vertex and (x, y)
                        Adds a new node moving by delta amount
                        from Vertex towards (x, y)
                        Adds an edge connecting new node and vertex
    ---------
    """
    def __init__(self, start_x, start_y, start_dx, start_dy, end_dx, end_dy, delta=1):
        self.nodes = [Node(start_x, start_y)]
        self.edges = []
        self.start_dx = start_dx
        self.start_dy = start_dy
        self.end_dx = end_dx
        self.end_dy = end_dy
        self.delta = delta

    def get_points(self):
        return np.array([node.x for node in self.nodes]), np.array([node.y for node in self.nodes])

    def random_configuration(self):
        ########## Begin_Citation [2] ##########
        # np.random.seed(42)

        N = 2 # x and y coordinates
        rand_vals = np.random.randint(0, 101, size=N)

        ########## End_Citation [2] ##########
        return rand_vals

    def nearest_vertex(self, q_rand):
        assert len(self.nodes) > 0
        shortest_distance = float('inf')
        nearest_node = None

        for node in self.nodes:
            dist = self.euclidean_distance(np.array([node.x, node.y]), q_rand)

            if dist < shortest_distance:
                shortest_distance = dist
                nearest_node = node

        return nearest_node


    def euclidean_distance(self, q_one, q_two):
        return np.linalg.norm(q_one - q_two)
    
    def new_configuration(self, nearest_vertex, random_node):
        current_position = np.array([nearest_vertex.x, nearest_vertex.y])
        goal_position = np.array(random_node)

        direction_vector = goal_position - current_position
        distance_to_goal = np.linalg.norm(direction_vector)

        if distance_to_goal > 0:
            direction_vector = direction_vector / distance_to_goal  

        step_size = min(self.delta, distance_to_goal)

        new_position = current_position + direction_vector * step_size

        return Node(new_position[0], new_position[1])
    
    def add_vertex(self, new_node):
        if self.get_vertex(new_node) == -1:
            self.nodes.append(new_node)

    def get_vertex(self, node):
        for v in self.nodes:
            if v.x == node.x and v.y == node.y:
                return v
        
        return -1

    def add_edge(self, node1, node2):
        new_edge = Edge(x1=node1.x, y1=node1.y, x2=node2.x, y2=node2.y)
        if self.get_edge(new_edge) == -1:
            self.edges.append(new_edge)

    def get_edge(self, edge):
        for e in self.edges:
            if e.x1 == edge.x1 and e.x2 == edge.x2 and e.y1 == edge.y1 and e.y2 == edge.y2:
                return e
        
        return -1
