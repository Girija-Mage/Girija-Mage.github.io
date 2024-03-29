from __future__ import print_function                    #ensures compatibility in Python versions 3.x and 2.x
import collections                                       #module containing number of container data types
import math                                              #mathematical functions
import operator                                          #exports a set of efficient functions
import networkx as nx                                    #creating & manipulating graphs & networks
from preprocess import cleanText                         #preprocessing
import os
from app import app


window = 10                                              #declarations
numberofSentences = 6
nodeHash = {}
textRank = {}
sentence_dictionary = collections.defaultdict(dict)
size = 0
sentences = []


def generatepositionaldistribution():
    '''
        Creates a weighted positional distribution of sentence scores based on their position in the text corpus
    '''
    global nodeHash, sentence_dictionary, sentences, size
    positional_dictionary = collections.defaultdict(dict)
    count = 0
    for i in sentence_dictionary.keys():
        for j in range(0, len(sentence_dictionary[i])):
            count += 1
            position = float(count) / (float(size) + 1.0)
            positional_dictionary[i][j] = 1.0 / (math.pi * math.sqrt(position * (1 - position)))
            word = sentence_dictionary[i][j]
            if word in nodeHash:
                if nodeHash[word] < positional_dictionary[i][j]:
                    nodeHash[word] = positional_dictionary[i][j]
            else:
                nodeHash[word] = positional_dictionary[i][j]


def textrank():
    '''
        Generates a graph based ranking model for the tokens
    :re turn: Keyphrases that are most relevant for generating the summary.
    '''
    global sentence_dictionary, nodeHash, textRank
    graph = nx.Graph()
    graph.add_nodes_from(nodeHash.keys())
    for i in sentence_dictionary.keys():
        for j in range(0, len(sentence_dictionary[i])):
            current_word = sentence_dictionary[i][j]
            next_words = sentence_dictionary[i][j + 1:j + window]
            for word in next_words:
                graph.add_edge(current_word, word, weight=(nodeHash[current_word] + nodeHash[word]) / 2)
    textRank = nx.pagerank(graph, weight='weight')
    keyphrases = sorted(textRank, key=textRank.get, reverse=True)[:n]
    return keyphrases


def summarize(filePath, keyphrases, numberofSentences):
    '''
        Generates the summary and writes the summary to the file.
    :param filePath: path of file to be used for summarization.
    :param keyphrases: Extracted keyphrases
    :param numberofSentences: Number of sentences needed as a summary
    :output: Writes the summary to the file
    '''
    global textRank, sentence_dictionary, sentences
    sentenceScore = {}
    for i in sentence_dictionary.keys():
        position = float(i + 1) / (float(len(sentences)) + 1.0)
        positionalFeatureWeight = 1.0 / (math.pi * math.sqrt(position * (1.0 - position)))
        sumKeyPhrases = 0.0
        for keyphrase in keyphrases:
            if keyphrase in sentence_dictionary[i]:
                sumKeyPhrases += textRank[keyphrase]
        sentenceScore[i] = sumKeyPhrases * positionalFeatureWeight
    sortedSentenceScores = sorted(sentenceScore.items(), key=operator.itemgetter(1), reverse=True)[:numberofSentences]
    sortedSentenceScores = sorted(sortedSentenceScores, key=operator.itemgetter(0), reverse=False)
    
    with open(os.path.join(app.config['DOWNLOAD_FOLDER'], 'pos_textrank.txt'), "w",encoding="utf-8") as outFile:
        for i in range(0, len(sortedSentenceScores)):
            outFile.write(sentences[sortedSentenceScores[i][0]] + "\n")
        outFile.close()
    
    
def posTextRank(arg1, arg2, arg3):
    '''
    :param arg1: path to the file containing the text to be summarized
    :param arg2: Number of sentences to be extracted as summary
    :param arg3: size of the window to be used in the co-occurance relation
    '''
    global window, n, numberofSentences, textRank, sentence_dictionary, size, sentences
    if arg1 != None and arg2 != None and arg3 != None:
        sentence_dictionary, sentences, size = cleanText(arg1)
        window = int(arg3)
        numberofSentences = int(arg2)
        n = int(math.ceil(min(0.1 * size, 7 * math.log(size))))
        generatepositionaldistribution()
        keyphrases = textrank()
        summarize(arg1, keyphrases, numberofSentences)
    else:
        print("not enough parameters")



