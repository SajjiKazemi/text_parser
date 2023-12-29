import re

def parse_input(line: str):
    
    """Parse input line into command, street name, and vertices"""

    inputs = re.split("\s", line)
    cmd = inputs[0]
    inputs = re.split('"', line)
    street_name = inputs[1]
    vertices = re.split('\s', inputs[2].strip())
    return cmd, street_name, vertices