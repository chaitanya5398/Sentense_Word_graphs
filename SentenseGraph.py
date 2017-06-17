from preprocessing import *
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
word_set = set(filtered_words)
word_dict = {}
sent_dict = {}


cnt=0

#Assigning numbers for the words along neg axis.
for j in word_set:
    word_dict[j] = cnt
    cnt = cnt+1

word_sent_list = [[] for p in range(cnt) ]  #The list which stores all the sentenses having the word with index = -1*wordindex.


#Sentense Ordering is according to the tuple sentense_list.
cnt=0
for j in sentense_list:
    cnt += 1
    for p in j:
        word_sent_list[word_dict[p]].append(cnt)

nodes = [j+1 for j in range(cnt)]
edges = []


#Making the edge tuple
for p in word_sent_list:
    n = len(p)
    for i in range(n):
        for j in range(i+1,n):
            t = (p[i],p[j])
            tt = (p[j],p[i])
            if (t not in edges) and (tt not in edges):
                edges.append(t)

#adding nodes and edges
G.add_nodes_from(nodes)
for j in edges:
    G.add_edge(*j)

#Plotting the graph.
nx.draw(G)
plt.show()

    
