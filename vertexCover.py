import sys
import re
import numpy as np

from helpers import *

class vertexCover:
    def __init__(self):
        self.vertices = {}
        self.intersections = {}
        self.edges = []
        self.streets = {}
    
    def add_street(self, name: str, vertices_str: list):
        vertices = []
        for vertex in vertices_str:
            x_arg = int(re.split("[(]", (re.split(",",vertex)[0]))[1])
            y_arg = int(re.split("[)]", (re.split(",",vertex)[1]))[0])
            vertices.append((x_arg, y_arg))
        self.streets[name] = vertices

    def add_edge(self, vertex1_index, vertex2_index):
        self.edges.append(f"<{vertex1_index},{vertex2_index}>")
        return

    def add_vertex(self, vertex):
        index = len(self.vertices)
        self.vertices[index] = vertex

    def update_vertices(self):
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
                                    self.vertices[len(self.vertices)+1] = end1_line1
                                    self.vertices[len(self.vertices)+1] = end2_line1
                                    self.vertices[len(self.vertices)+1] = end1_line2
                                    self.vertices[len(self.vertices)+1] = end2_line2
                                    self.vertices[len(self.vertices)+1] = intersection_point
                                    vertices_indices = list(self.vertices.keys())
                                    self.intersections[f'intn{len(self.intersections)}v{int((vertices_indices)[-1])}'] = \
                                        [int((vertices_indices)[-5]), int((vertices_indices)[-4])\
                                         , int((vertices_indices)[-3]), int((vertices_indices)[-2])]
        #self.vertices = list(set(self.vertices))
        self.organize_intersections()       # Organize vertices (inside organize_intersections)
                                            # and intersections


    def organize_vertices(self):
        intermediate = {}
        for vertex in self.vertices:
            if self.vertices[vertex] not in intermediate.values():    
                intermediate[len(intermediate)+1] = self.vertices[vertex]
        return intermediate

    def organize_intersections(self):
        intermediate = self.organize_vertices()
        for vertex in self.vertices:
            repeated_vertex = self.vertices[vertex]
            for vertex2 in intermediate:
                if intermediate[vertex2] == repeated_vertex:
                    key_vertex2 = vertex2
                    for intersection in self.intersections:
                        if vertex in self.intersections[intersection]:
                            vertex_index = self.intersections[intersection].\
                                index(vertex)
                            self.intersections[intersection][vertex_index] = key_vertex2

        intersection_keys = list(self.intersections.keys())
        for intersection_key in intersection_keys:
            value_in_vertices = self.vertices[int(re.split("[v]", intersection_key)[1])]
            for key_intermediate, value_intermediate in intermediate.items():
                if value_in_vertices == value_intermediate and key_intermediate !=\
                      int(re.split("[v]", intersection_key)[1]):
                        value_to_change = self.intersections[intersection_key]
                        self.intersections[f'intn{len(self.intersections)}v{key_intermediate}']\
                              = value_to_change
                        self.intersections[intersection_key] = None
        intersection_keys = list(self.intersections.keys())
        for intersection_key in intersection_keys:
            if self.intersections[intersection_key] == None:
                del self.intersections[intersection_key]
        self.vertices = intermediate

    def get_edges(self):
        keys = list(self.intersections.keys())
        if len(keys) < 1:
            return []
        if len(keys) == 1:
            return [f"<0,1>"] 

    def get_streets(self):
        return self.streets