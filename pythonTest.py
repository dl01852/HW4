from utilsClasses import Vertex,Edge
from collections import defaultdict
from pprint import pprint
from itertools import chain

# code written by David Lewis.

v = Vertex('1')
v2 = Vertex("0")
e = Edge(v, v2)

num_Vertex = None
num_Edges = None
dict_Vertex = {}
setVertex = set()
setEdges = set()


# strip off the \n and replace the tab with a space and then split on
file = [line.strip().replace('\t', ' ').split(' ') for line in open('ran25.txt')]

for pair in file:
    if pair == file[0]:
        num_Vertex = pair[0]
        num_Edges = pair[1]
        print("Vertex total: %s\nEdge Total: %s" % (num_Vertex, num_Edges))
    else:
        v1 = Vertex(pair[0])
        v2 = Vertex(pair[1])
        tempV1 = None
        tempV2 = None

        # the gist of the following code. A dictionary will hold unique objects of vertexes as well as in set called
        # setVertexes. As i read each line (edge) i'll create a vertex for edges.
        # before placing them in the setEdges set i check to make sure the vertex(s) doesn't already exist in the set.
        # if either of the vertex(s) already exist, i'll pull that object from the dictionary to store that in
        # the setEdges set since i can't pull it from the setEdges set(sets doesnt allow that)
        # minor optimization might be to check the dictionary first for the name before even creating vertexes
        # on line 25/26
        if v1 in setVertex:
            if v2 in setVertex:  # v1 and v2 are in the set already.(use temp1 and temp2)
                tempV1 = dict_Vertex[v1.name]
                tempV2 = dict_Vertex[v2.name]
                tempV1.add_neighbor(tempV2)

                edge = Edge(tempV1, tempV2)
                setEdges.add(edge)

            else:  # v1 is in but not v2. (use temp1, v2)
                tempV1 = dict_Vertex[v1.name]
                edge = Edge(tempV1, v2)
                tempV1.add_neighbor(v2)

                setEdges.add(edge)
                setVertex.add(v2)
                dict_Vertex.update({v2.name: v2})

        elif v2 in setVertex:  # v2 is in but not v1(use v1, temp2)
            tempV2 = dict_Vertex[v2.name]
            edge = Edge(v1, tempV2)
            v1.add_neighbor(tempV2)  # add your neighbor..
            setEdges.add(edge)
            setVertex.add(v1)
            dict_Vertex.update({v1.name: v1})

        else:  # neither v1 nor v2 are in (use v1, v2)
            dict_Vertex.update({v1.name: v1, v2.name: v2})
            setVertex.add(v1)
            setVertex.add(v2)
            edge = Edge(v1, v2)
            v1.add_neighbor(v2)
            setEdges.add(edge)


#print(*setVertex, setEdges, sep='\n')

R = set()
P = set(setVertex)
X = set()
answer =[]


def bron_kerbosch(p, r, x):
    listP = sorted(list(p), key=lambda ve: ve.name)
    if p | x == set():
        answer.append(r)
        return r
    for vertex in listP[:]:
        r_new = set(r)
        r_new.add(vertex)
        bron_kerbosch(p & vertex.neighbors, r_new, x & vertex.neighbors)
        listP.remove(vertex)
        x.add(vertex)


# test code to get adjacent nodes of a particular vertex
vertex0 = dict_Vertex['0']
print("Nodes adjacent to %s: " % vertex0.name, sorted(vertex0.neighbors, key=lambda g: g.name))
print("compliment of vertex %s: " % vertex0.name, sorted((setVertex - vertex0.neighbors),key=lambda r: r.name))

# bron_kerbosch(P, R, X)
# # clique = sorted(max(answer),key=lambda vertex: vertex.name)
# # print(*[v.name for v in clique])
# cliques = [x for x in answer if len(x) >= len(max(answer, key=len))] # list comprehension to only get the cliques with the highest number in their set.
# a = [sorted([v.name for v in x]) for x in cliques]  # after we have the set(s) of maxi cliques, sort the order and grab their name then print
# print(a)
# maximum_clique = len(max(a,key=len)) # max number of vertex's in the highest clique.
# Total_clique = len(a) # the amount of sets that had the max clique.
# print("max cliques: %s\nTotal Max cliques: %s" % (maximum_clique, Total_clique))
