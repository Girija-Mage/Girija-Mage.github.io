from preprocess import cleanText             #preprocessing
import networkx                              #creating & manipulating graphs & networks
import itertools                             #iterator functions for efficient looping
import os
import collections
import re, math
from app import app


sentence_dictionary = collections.defaultdict(dict)         #declarations
sentences = [] 


class Similarity():
    def compute_cosine_similarity(self, string1, string2):
         intersection = set(string1.keys()) & set(string2.keys())
         numerator = sum([string1[x] * string2[x] for x in intersection])

         sum1 = sum([string1[x]**2 for x in string1.keys()])
         sum2 = sum([string2[x]**2 for x in string2.keys()])

         denominator = math.sqrt(sum1) * math.sqrt(sum2)
         if not denominator:
            return 0.0
         else:
            return round(numerator/float(denominator),4)

    def text_to_vector(self,text):
        WORD = re.compile(r'\w+')
        words = WORD.findall(text)
        return collections.Counter(words)


def getCosineSimilarity(sentenceID1,sentenceID2):
    similarity = Similarity()
    
    text1 = " ".join(sentence_dictionary[sentenceID1])
    text2 = " ".join(sentence_dictionary[sentenceID2])
    
    vector1 = similarity.text_to_vector(text1)
    vector2 = similarity.text_to_vector(text2)
    
    cosine = similarity.compute_cosine_similarity(vector1, vector2)
    return cosine


def generateGraph(nodeList):
    '''
    graph generation
    '''
    graph = networkx.Graph()            #creating an empty graph
    graph.add_nodes_from(nodeList)      #adding nodes
    edgeList = list(itertools.product(nodeList, repeat=2))         #cartesian product
    for edge in edgeList:
        graph.add_edge(edge[0], edge[1], weight=getCosineSimilarity(edge[0], edge[1]))   #adding edge with weights
    return graph


def cosineTextRank(filePath, summarySentenceCount):            
    '''
    summary generation using similarity between sentences
    '''
    global sentence_dictionary, sentences
    
    sentence_dictionary, sentences, size = cleanText(filePath)   #input after preprocessing 
    
    graph = generateGraph(list(sentence_dictionary.keys()))      #keys are sentence ids

    pageRank = networkx.pagerank(graph)      #computes ranking of nodes in graph,return type is a dictionary

    output = "\n".join([sentences[sentenceID] for sentenceID in sorted(sorted(pageRank, key=pageRank.get, reverse=True)[:summarySentenceCount])])

    with open(os.path.join(app.config['DOWNLOAD_FOLDER'], 'cos_textrank.txt'), "w",encoding="utf-8") as outFile:
        outFile.write(output)
        outFile.close()
        

