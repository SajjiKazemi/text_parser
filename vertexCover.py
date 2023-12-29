import sys
import re
import numpy as np

from helpers import *

class vertexCover:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.streets = {}
    
    def add_street(self, name: str, vertices_str: list):
        vertices = []
        for vertex in vertices_str:
            x_arg = int(re.split("[(]", (re.split(",",vertex)[0]))[1])
            y_arg = int(re.split("[)]", (re.split(",",vertex)[1]))[0])
            vertices.append((x_arg, y_arg))
        self.streets[name] = vertices

    def get_intersecions(self):
        keys = list(self.streets.keys())
        while len(keys) > 1:
            street1 = keys[0]
            keys.remove(street1)
            for street2 in keys:
                if street1 != street2:
                    for i in range(len(self.streets[street1])):
                        for j in range(len(self.streets[street2])):
                            if i != len(self.streets[street1])-1 \
                                and j != len(self.streets[street2])-1:
                                end1_line1 = self.streets[street1][i]
                                end2_line1 = self.streets[street1][i+1]
                                line1 = create_line(end1_line1, end2_line1)
                                end1_line2 = self.streets[street2][j]
                                end2_line2 = self.streets[street2][j+1]
                                line2 = create_line(end1_line2, end2_line2)
                                intersection_point = intersection(line1, line2)
                                if intersection_point and check_intersection(
                                    intersection_point, end1_line1, end2_line1
                                    , end1_line2, end2_line2):
                                    self.vertices.append(end1_line1)
                                    self.vertices.append(end2_line1)
                                    self.vertices.append(end1_line2)
                                    self.vertices.append(end2_line2)
                                    self.vertices.append(intersection_point)
        self.vertices = list(set(self.vertices))
        return self.vertices
    
    def get_streets(self):
        return self.streets