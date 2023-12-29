#!/usr/bin/env python3
import sys
import re

from helpers import *
from vertexCover import *

def main():

    # Create an instance of vertexCover
    vertex_cover = vertexCover()

    # Read input from stdin and print it to stdout
    # Note: input is terminated by EOF (Ctrl+D on Linux)
    while True:
        line = sys.stdin.readline()
        if line == "":
            break
        print("reading a line:", line)
        
       # split the line into words
        cmd, street_name, vertices = parse_input(line)

        if cmd == "add":
            vertex_cover.add_street(street_name, vertices)
            print(vertex_cover.get_streets())
            print("Added a street")
        elif cmd == "gg":
            vertex_cover.update_vertices()

        
    print("Finished reading input")
    sys.exit(0)


if __name__ == "__main__":
    main()
