from __future__ import print_function      # ensures compatibility in Python versions 3.x and 2.x
from __future__ import unicode_literals
from tokenization import tokenize          #importing functions
from stopwords import readStopWords
import collections                         #module containing number of container data types


sentence_dictionary = collections.defaultdict(dict)         #declarations
sentences = [] 


def cleanText(filename):                      #preprocessing of text
    '''
    Tokenize, Remove stopwords and reduce the words to their stem
    :param filename: path of file to be preprocessed
    '''
    global sentence_dictionary,sentences
    readStopWords()
    sentence_dictionary,sentences = tokenize(filename)
    
    size = 0
    for i in range(0, len(sentence_dictionary)):
        size += len(sentence_dictionary[i])
    
    return sentence_dictionary, sentences, size





