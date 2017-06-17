# Sentense_Word_graphs
This is a repository having the basic NLP code using the nltk, networkx , matplotlib of python.

preprocess.py
The program takes an input text and 
1) Removes stop words.
2) Lammetizes the words.
3) Gets the preprocessed lists required for the next two programs which are basically tokenized word ans Sentense vectors.

WordGraph.py
1) Constructs Word Graphs - The nodes are unique set of words and there is an edge between all adjacent words in the text given.

SentenseGraph.py
1) Constructs Sentense Graphs - The nodes are sentenses and there is an edge between S1 and S2 of weight x if theese two sentences share x words in common.
