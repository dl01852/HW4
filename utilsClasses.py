class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = set()

    def __str__(self):
        return "%s" % self.name

    def __repr__(self): # this function depends on the has! this determines if an object is unqieu or not.
        return "%s:" % self.name

    def __eq__(self, other):
        if type(other) == Vertex:
            return other.name == self.name

    def __hash__(self):
        return hash(self.__repr__())

    def add_neighbor(self, vertex):  # each vertex will keep track of it's neighbors.
        self.neighbors.add(vertex)


# EDGE CLASS
class Edge:
    def __init__(self, vertex1, vertex2):
        self.vertex1 = vertex1
        self.vertex2 = vertex2

    def __str__(self):
        return "%s -> %s" % (self.vertex1.name, self.vertex2.name)

    def __repr__(self):
        return "%s: -> %s" % (self.vertex1.name, self.vertex2.name)
