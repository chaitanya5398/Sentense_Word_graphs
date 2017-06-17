from preprocessing import *
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
word_set = set(filtered_words)
word_dict = {}

cnt=0

#Assigning node numbers for the words.
for j in word_set:
    word_dict[j] = cnt
    cnt = cnt+1

print "\nThe Dictionary of the word map."
print word_dict
print "\n"
    
#Forming the links.
nodes = [j+1 for j in range(cnt)]
adjacency = [ [0 for j in range(cnt)] for j in range(cnt) ]
edge_tuples = []

print "Nodes\n"
print G.nodes()
print "Edges\n"
print G.edges()


for j in range(len(filtered_words) - 1):
    adjacency[word_dict[filtered_words[j]]][word_dict[filtered_words[j+1]]] = 1
    edge_tuples.append((word_dict[filtered_words[j]]+1,word_dict[filtered_words[j+1]]+1))

#adding nodes and edges
G.add_nodes_from(nodes)
for j in edge_tuples:
    G.add_edge(*j)

#Plotting the graph.
nx.draw(G)
plt.show()
