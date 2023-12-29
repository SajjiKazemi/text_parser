import re

def parse_input(line: str):
    
    """Parse input line into command, street name, and vertices"""

    inputs = re.split("\s", line)
    cmd = inputs[0]
    inputs = re.split('"', line)
    street_name = inputs[1]
    vertices = re.split('\s', inputs[2].strip())
    return cmd, street_name, vertices

def create_line(point1, point2):
    """Create a line from two points, considering the line equation Ax + By + C = 0"""
    A = (point1[1] - point2[1])
    B = (point2[0] - point1[0])
    C = (point1[0]*point2[1] - point2[0]*point1[1])
    return A, B, -C
    