import sys
import numpy as np

class vertexCover:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.streets = {}
    
    def add_street(self, name: str, vertices: list):
        self.streets[name] = vertices
    
    def get_streets(self):
        return self.streets