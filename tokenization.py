import collections                         #module containing number of container data types
import copy                                #provides generic shallow and deep copy operations  
import io                                  #stream handling
import nltk                                #natural language processing
import re                                  #regular expression
from nltk.tokenize import sent_tokenize
nltk.download('punkt')                     #sentence tokenizer
from stopwords import removeStopWords      #import functions
from stemming import stemmerMarathi

                           
sentences = []                             #declarations
sentences_processing = []
sentence_dictionary = collections.defaultdict(dict)
stemWords = {}


def tokenize(filename):
    '''
    Tokenizes the sentences and words
    :param filename: path of the file containing the text to be summarized
    '''
    global sentences, sentences_processing, sentence_dictionary
    with io.open(filename, "r", encoding="utf-8") as inputFile:
        data = inputFile.read()
        inputFile.close()
        
    sentences = sent_tokenize(data)
    sentences_processing = copy.deepcopy(sentences)
    
    counter = 0
    for sentence in sentences_processing:
        sentence = sentence[:-1]
        sentence = re.sub(',|\.|-|\(|\)', ' ', sentence)           #replace punctuations by space
        tokens = sentence.strip().split()                          #remove spaces,newline
        actualTokens = removeStopWords(tokens)                     #stopwordsremoval
        stemmedTokens = stemmerMarathi(actualTokens)               #stemming
        sentence_dictionary[counter] = stemmedTokens
        counter += 1
        
    return sentence_dictionary,sentences   











