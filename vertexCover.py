import sys
import re
import numpy as np

class vertexCover:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.streets = {}
    
    def add_street(self, name: str, vertices_str: list):
        vertices = []
        for vertex in vertices_str:
            x_arg = int(re.split("[(]", (re.split(",",vertices_str[0])[0]))[1])
            y_arg = int(re.split("[)]", (re.split(",",vertices_str[0])[1]))[0])
            vertices.append((x_arg, y_arg))
        self.streets[name] = vertices

    def get_streets(self):
        return self.streets