from preprocess import cleanText             #preprocessing
import networkx                              #creating & manipulating graphs & networks
import itertools                             #iterator functions for efficient looping
import math                                  #mathematical functions
from app import app
import os


sentenceDictionary = {};


def getSimilarity(sentenceID1, sentenceID2):
    '''
    similarity calculation
    '''
    commonWordCount = len(set(sentence_dictionary[sentenceID1]) & set(sentence_dictionary[sentenceID2]))            #len() returns length of string set() constructs set & returns it
    denominator = math.log(len(sentence_dictionary[sentenceID1])) + math.log(len(sentence_dictionary[sentenceID2])) #log base e
    return commonWordCount/denominator if denominator else 0


def generateGraph(nodeList):
    '''
    graph generation
    '''
    graph = networkx.Graph()            #creating an empty graph
    graph.add_nodes_from(nodeList)      #adding nodes
    edgeList = list(itertools.product(nodeList, repeat=2))         #cartesian product
    for edge in edgeList:
        graph.add_edge(edge[0], edge[1], weight=getSimilarity(edge[0], edge[1]))   #adding edge with weights
    return graph


def simTextRank(filePath, summarySentenceCount):            
    '''
    summary generation using similarity between sentences
    '''
    global sentence_dictionary
    sentence_dictionary = {};
    sentences = []

    sentence_dictionary, sentences, size = cleanText(filePath)  #input after preprocessing 

    graph = generateGraph(list(sentence_dictionary.keys()))      #keys are sentence ids

    pageRank = networkx.pagerank(graph)      #computes ranking of nodes in graph,return type is a dictionary

    output = "\n".join([sentences[sentenceID] for sentenceID in sorted(sorted(pageRank, key=pageRank.get, reverse=True)[:summarySentenceCount])])

    with open(os.path.join(app.config['DOWNLOAD_FOLDER'], 'sim_textrank.txt'), "w",encoding="utf-8") as outFile:
        outFile.write(output)
        outFile.close()

