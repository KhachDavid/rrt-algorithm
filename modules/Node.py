#
#  Node.py
#  RRT Algorithm
#
#  Created by David Khachatryan on 9/17/24.
#

class Node:
    """
    Attributes
    ----------
    neighbors: List of Node objects
    x: X coordinate of this node
    y: Y coordinate of this node
    Functions
    ---------

    """
    def __init__(self, x, y, neighbors=[]):
        self.neighbors = neighbors
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"