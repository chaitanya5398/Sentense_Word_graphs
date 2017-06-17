import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

inp = raw_input("Please give the input to be analysed: ")

stop_words = set(stopwords.words('english'))
sentense_tokens = sent_tokenize(inp)
word_tokens = word_tokenize(inp)
lemmatizer = WordNetLemmatizer()

print 'The sentense tokens\n'
print sentense_tokens
print "\n"

lemmated_words = []
filtered_words = []
sentense_list =  []

#Removing punctuations
word_tokens=[word.lower() for word in word_tokens if word.isalpha()]

#This is for the sentense pre-processing.
for j in sentense_tokens:
    p = word_tokenize(j)
    tmp=[]
    for l in p:
        l = l.lower()
        if l.isalpha():
            l = lemmatizer.lemmatize(l)
            if l not in stop_words:
                tmp.append(l)
    tmp = list(set(tmp))
    sentense_list.append(tmp)

print "The removed snetense words."
for l in sentense_list:
    print "\n New Sentense\n"
    print l


#This is for the words preprocessing.
#lemmatizing the words.
for j in word_tokens:
    p = lemmatizer.lemmatize(j)
    lemmated_words.append(p)
lemmated_words = list(set(lemmated_words))
    
#For removing the stop words.
for w in lemmated_words:
    if w not in stop_words:
        filtered_words.append(w)

print "Original input\n" 
print(word_tokens)
print "lemmated words\n"
print (lemmated_words)
print "Lemmatized and stopword removed words.\n"
print(filtered_words)
