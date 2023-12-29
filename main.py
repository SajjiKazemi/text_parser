#!/usr/bin/env python3
import sys

def main():
    # Read input from stdin and print it to stdout
    # Note: input is terminated by EOF (Ctrl+D on Linux)
    while True:
        line = sys.stdin.readline()
        if line == "":
            break
        print("reading a line:", line)

    print("Finished reading input")
    sys.exit(0)


if __name__ == "__main__":
    main()
