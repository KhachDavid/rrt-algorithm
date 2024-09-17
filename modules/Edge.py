#
#  Edge.py
#  RRT Algorithm
#
#  Created by David Khachatryan on 9/17/24.
#
import numpy as np

class Edge:
    """
    Attributes
    ----------
    x1: X coordinate of point one
    y1: Y coordinate of point one
    x2: X coordinate of point two
    y2: Y coordinate of point two

    Functions
    ---------

    """
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_point_one(self):
        return np.array([self.x1, self.y1])
    
    def get_point_two(self):
        return np.array([self.x2, self.y2])