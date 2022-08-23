"""Graphs are perfect for moduling real world objects because it provides relationships between two or more objects
there are two main types or graphs, undirected graphs and a directed graph, it consist of vertices and edges connected to those 
vertices to show the relationship """

# weighted Edges- are used to represent the Distance or Time between Nodes
# dense Graphs- in a dense graph every vertex may be connectted to every other vertex, the  |E|(number edges) = |V|^2
# sparse graphs- in a sparse graph each vertice has one edge


# the two most common ways to impliment graphs:

# ADJACENCY LIST - Lists of neighbors stored in each vertex
# pros:
# Faster and uses less space for a really sparse Graphs
# cons: Slower for Dense graphs

# ADJACENCY MATRIX- matrix of neighbors stored centrally in graph object
# a Adjacency Matrix takes up |v|^2 space regardless of how dense the graph is
# pros:
# if we have weighted Edges, it will be much easier to impliment a graph using an adjacency matrix, since we can just store the weight in the matrix
# faster for Dense grpahs
# cons: uses more space


# Python Implimentation: #ADJACENCY LIST

# t
class Vertex:
    def __init__(self, n):  # the constructor to create a new vertex
        # creats two attributes for the vertex
        self.name = n
        self.neighbors = set()  # creates an empty set for the neighbors

    # we can pass in the name of the vertex and it will add it to the neighbors
    def add_neighbor(self, v):
        self.neighbors.add(v)


class Graph:
    vertices = {}  # each graph object stores a vertices dictionary of all the vertices, format vertex name as the key and the vertex object as the valu e

    def add_vertex(self, vertex):
        # checks if the data to be added is an instance of the Vertex class and the name is not already in the dictionary
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:

            # we add is as a key value pair to the Vertices
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        # checks to see if they are both real vertices that can connect to a vertex
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v)  # add u to v neighbor list
            self.vertices[v].add_neighbor(u)  # and v to u neighbot list
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key, sorted(list(self.vertices[key].neighbors)))


# test code

mygraph = Graph()
a = Vertex('A')
mygraph.add_vertex(a)
mygraph.add_vertex(Vertex('B'))

# using ord to iterate through the numerical equivalent of A through K
for i in range(ord('A'), ord('K')):
    # using chr to get the character equivalent
    mygraph.add_vertex(Vertex(chr(i)))


edges = ['AB', 'AE', 'BF', 'CG', 'DE', "DH", 'EH', 'FG', 'FI', 'FJ', "GJ"]

for edge in edges:
    mygraph.add_edge(edge[0], edge[1])

mygraph.print_graph()
