

class Vertex:  # the vertex class in the matrix implimentation is really simple all it has is the name
    def __init__(self, n):
        self.name = n

# the graph class is where the bulk of the code is,
# we have 3 key attributes:
#  a dictionary with vertex_name: vertex_object.
# a 2 dimentional list(matrix) of edges. 0 for no edge and 1 for 1 edge
# edge_ indices- a dictionary with vertex_name:list_index(eg. A:0) to access edges


class Graph:
    vertices = {}
    edges = []
    edge_indices = {}

    def add_vertex(self, vertex):
        # checks to see if we are in a valid vertex
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            # if we are we will add the vertex in the dictionary via {vertex.name:vertex} in the vertices dictionary
            self.vertices[vertex.name] = vertex
            for row in self.edges:  # using a for loop to append a collum to the right most side of the matrix
                row.append(0)  # appending zero
            # here we are appending a row of zeros at the very bottom of the matrix , however many edges there are we are going to add a zero at the bottom
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[vertex.name] = len(
                self.edge_indices)  # updating the edge vertices
            return True
        else:
            return False

    def add_edge(self, u, v, weight=1):
        # checks to see that u and v passed are in the vertices dictionary
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False

    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):
            print(v + ' ', end='')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end=' ')
            print(' ')

# test code

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
