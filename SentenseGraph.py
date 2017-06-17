from preprocessing import *
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
word_set = set(filtered_words)
word_dict = {}
sent_dict = {}
node_labels = {}

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
        word_sent_list[word_dict[p]] = list(set(word_sent_list[word_dict[p]]))


adj_mat = [ [0 for j in range(cnt) ] for j in range(cnt) ]
nodes = [j+1 for j in range(cnt)]
edges = []


#Making the edge tuple
for p in word_sent_list:
    n = len(p)
    for i in range(n):
        for j in range(i+1,n):
            adj_mat[ min(p[i],p[j]) -1 ][ max(p[i],p[j]) -1 ] += 1

            
#adding nodes and edges
print "\nThe Adjacency matrix for the Sentense graph.\n"
for n in nodes:
    G.add_node(n)
    node_labels[n] = n
    
for a in range(cnt):
    for b in range(cnt):
        if adj_mat[a][b] != 0:
            G.add_edge(a+1,b+1)
            G[a+1][b+1]['weight'] = adj_mat[a][b]
        print adj_mat[a][b] , " ",
    print "\n"

print "Edges\n"
print G.edges()
            
#Plotting the graph.
pos = nx.circular_layout(G)
nx.draw(G,pos)
e_labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=e_labels)
nx.draw_networkx_labels(G,pos,node_labels)
plt.show()
