"""
Graphs are a set of nodes, called VERTICES, interconnected by 'links' or 'EDGES'
----------------------------
BIG O:

--------------------------

TYPES of Graphs:
 -Trees are a type of Graph (acyclical), and all nodes must be connected
 - Graphs can be cyclical, and nodes can be independent.
 -Directed Graphs: sepcific direction (acyclical?)
 -  Undirected : assume the relationship is mutual
 - Weighted: have numeric value associated with the edges (directed or undirected)
--------------------------------
EDGES:
Can be WEIGHTED (edges are given a number), or NON-WEIGHTED
can DIRECTIONAL (one vertex point to another), or BI-DIRECTIONAL(both point to each other)
---------------------------------------
GRAPH ADJACENCY MATRIX:
    Connections between vertices are represented by a number. If it is non-weighted, you will have 0's and 1's, if weighted, you will have the "weights" and 0's.
    Bi-directional Graph Adjancency Matrices are mirrored, with a 45degree row of zeros, indicated that the vertices cannot attach to themselves.

UNWEIGHTED, BI-DIRECTIONAL
  A B C D E
A 0 1 0 0 1
B 1 0 1 0 0
C 0 1 0 1 0
D 0 0 1 0 1
E 1 0 0 1 0

WEIGHTED, BI-DIRECTIONAL:
  A B C D E
A 0 2 0 0 9
B 2 0 4 0 0
C 0 4 0 6 0
D 0 0 6 0 8
E 9 0 0 8 0
----------------------------------------------
GRAPH ADJACENCY LIST:
    represented with a DICTIONARY, rather than a MATRIX.
    The "key" is the vertex value, and the paired "value" is a list of the vertices it shares and edge with.
 
UNWEIGHTED, BI-DIRECTIONAL
{
    'A':['B','E'],
    'B':['A','C'],
    'C':['B','D'],
    'D':['C', 'E'],
    'E':['A','D']
}

-------------------------------------------------
USES: 
 - Social Network
 - Locations and distances: optimize routes
 - Graph databases
 - Searching and sorting algorithms
---------------------------------------
COMPLEXITY:
    Space comparison
        adjacency graph is O(|V|^^2) IOW, the number of vertices squared.
        adjacency list  is O(|V| + |E|) IOW, the count of vertices + the count of Edges. 

        The reason the graph is so less space efficient, is because you have to store all the empty vertices as 0.
    
    BIG O
    Adding a Vertex 
        Graph is O(|V|^^2), because you are essentially rewriting the entire graph for every addition
        List is O(1), because it is a simple dictionary insert, ie. 1 simple operation.
    Adding an Edge:
     Both are O(1): for a graph you append the new vertex to the corresponding list, and for the graph you need only change the corresponding 0's to 1's

------------------------------------------------------

Depth First Search (DFS)

Since graphs have cyles, we need to keep track of which nodes/vertices have been visited

Steps:
1. start at any vertex
2. Tracks current vertex to visited vertices list
3. For each current node's adjacent vertex:
  - if it has been visited -> ignore it
  - if not -> recursively perform DFS

Complexity: O(V + E) V = num of Vertices, E = num of edges.

"""


import queue


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertice(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, source, target):
        self.vertices[source].append(target)


# build a graph:
my_graph = Graph()
my_graph.add_vertice('David')
my_graph.add_vertice('Miriam')
my_graph.add_vertice('Martin')

my_graph.add_edge('David', 'Miriam')
my_graph.add_edge('David', 'Martin')
my_graph.add_edge('Miriam', 'Martin')

# Implementation of a wieghted graph:


class WeightedGraph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        # Set the data for the vertex
        self.vertices[vertex] = []

    def add_edge(self, source, target, weight):
        # Set the weight
        self.vertices[source].append([target, weight])


# Instance of a weighted graph:
my_graph = WeightedGraph()

# Create the vertices
my_graph.add_vertex('Paris')
my_graph.add_vertex('Toulouse')
my_graph.add_vertex('Biarritz')

# Create the edges
my_graph.add_edge('Paris', 'Toulouse', 678)
my_graph.add_edge('Toulouse', 'Biarritz', 312)
my_graph.add_edge('Biarritz', 'Paris', 783)


# Depth First Search implementation
graph = {
    '0': ['1', '2'],
    '1': ['0', '2', '3'],
    '2': ['0', '1', '4'],
    '3': ['1', '4'],
    '4': ['2', '3']
}


def dfs(visited_vertices, graph, current_vertex):
    if current_vertex not in visited_vertices:
        print(current_vertex)
        visited_vertices.add(current_vertex)
        for adjacent_vertex in graph[current_vertex]:
            dfs(visited_vertices, graph, adjacent_vertex)


class ExpressionTree:
    def __init__(self):
        self.root = None

    def pre_order(self, current_node):
        # Check if current_node exists
        if current_node:
            # Print the value of the current_node
            print(current_node.data)
            # Call pre_order recursively on the appropriate half of the tree
            self.pre_order(current_node.left_child)
            self.pre_order(current_node.right_child)


et = ExpressionTree()
et.pre_order(et.root)
