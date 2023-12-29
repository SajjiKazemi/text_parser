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
            if len(vertices) < 2:
                print('Error: You need at least two point a street', file=sys.stderr)
                continue
            vertex_cover.add_street(street_name, vertices)

        elif cmd == "mod":
            if len(vertices) < 2:
                print('Error: You need at least two point a street', file=sys.stderr)
                continue
            vertex_cover.mod_street(street_name, vertices)

        elif cmd == "rm":
            if len(vertex_cover.streets) == 0:
                print('Error: You need at least one street to remove', file=sys.stderr)
                continue
            vertex_cover.rm_street(street_name)

        elif cmd == "gg":
            if len(vertex_cover.streets) == 0:
                print('Error: You need at least one street to draw', file=sys.stderr)
                continue
            vertex_cover.update_vertices()
            vertex_cover.print_vertices()
            vertex_cover.print_edges()


    print("Finished reading input")
    # return exit code 0 on successful termination
    sys.exit(0)


if __name__ == "__main__":
    main()
