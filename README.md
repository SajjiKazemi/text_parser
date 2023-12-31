# Text Parser to Get the Streets' Information

## Overview

This Python project serves as a text parser designed to extract essential information about streets, such as their names and coordinates. It marks the initial phase of a broader project aimed at identifying a vertex cover for streets with intersections. This constitutes the first of a series of tasks within a comprehensive project. The ultimate goal is to determine the vertex cover of a randomly generated graph, addressing the Vertex Cover problem, a specific type of optimization problem in graph theory. For a brief understanding of the vertex cover concept, refer to [this link](https://en.wikipedia.org/wiki/Vertex_cover#:~:text=In%20graph%20theory%2C%20a%20vertex,every%20edge%20of%20the%20graph).

For this project, a few steps will be taken:
• Take as input a series of commands that describe streets.
• Use that input to construct a particular kind of undirected graph.

### Detailed Explanation

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/SajjiKazemi/input_parser.git
```

## Dependencies
Create a virtual environment using the provided my_env.yml file:

```bash
conda env create -f my_env.yml
```
Activate the environment:

```bash
conda activate my_env
```

## Usage

The input consists of lines, each specifying a command falling into one of four types: (1) add a street, (2) modify a street, (3) remove a street, and (4) generate a graph.

add: Adds a street, specified as: add "Street Name" (x1, y1) (x2, y2) . . . (xn, yn). Each (xi, yi) represents a GPS coordinate, interpreted as a polyline segment.

mod: Modifies the specification of a street, following the same format as 'add'.

rm: Removes a street, specified as: rm "Street Name".

gg: Outputs the corresponding graph.

Vertices correspond to intersections and endpoints of street segments that intersect with others.

## Contact
For any questions or feedback, feel free to reach out:

Email: sajjikazemi@uwaterloo.ca

LinkedIn: www.linkedin.com/in/sajjadkazemi
