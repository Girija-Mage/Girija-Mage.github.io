from preprocess import cleanText             #preprocessing
import networkx                              #creating & manipulating graphs & networks
import itertools                             #iterator functions for efficient looping
import collections
import os
from app import app


sentence_dictionary = collections.defaultdict(dict)         #declarations
sentences = [] 


class Similarity():
     def jaccard_similarity(self, string1, string2):
        intersection = set(string1).intersection(set(string2))
        union = set(string1).union(set(string2))
        return len(intersection)/float(len(union)) if union else 0
   

def getJaccardSimilarity(sentenceID1,sentenceID2):
    similarity = Similarity()
    
    token1 = sentence_dictionary[sentenceID1]
    token2 = sentence_dictionary[sentenceID2]
    
    jaccard = similarity.jaccard_similarity(token1,token2)
    return jaccard


def generateGraph(nodeList):
    '''
    graph generation
    '''
    graph = networkx.Graph()            #creating an empty graph
    graph.add_nodes_from(nodeList)      #adding nodes
    edgeList = list(itertools.product(nodeList, repeat=2))         #cartesian product
    for edge in edgeList:
        graph.add_edge(edge[0], edge[1], weight=getJaccardSimilarity(edge[0], edge[1]))   #adding edge with weights
    return graph


def jaccardTextRank(filePath, summarySentenceCount):            
    '''
    summary generation using similarity between sentences
    '''
    global sentence_dictionary, sentences
    
    sentence_dictionary, sentences, size = cleanText(filePath)   #input after preprocessing 

    graph = generateGraph(list(sentence_dictionary.keys()))      #keys are sentence ids

    pageRank = networkx.pagerank(graph)      #computes ranking of nodes in graph,return type is a dictionary

    output = "\n".join([sentences[sentenceID] for sentenceID in sorted(sorted(pageRank, key=pageRank.get, reverse=True)[:summarySentenceCount])])

    with open(os.path.join(app.config['DOWNLOAD_FOLDER'], 'jaccard_textrank.txt'), "w",encoding="utf-8") as outFile:
        outFile.write(output)
        outFile.close()
        


