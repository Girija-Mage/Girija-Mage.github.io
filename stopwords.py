import io                    #stram handling


stopwords = set()            #declarations


def readStopWords():
    '''
    Reads the stopwords from the file
    '''
    with io.open("stopwords.txt", encoding='utf-8') as textFile:
        for line in textFile:
            words = line.lower().strip()
            stopwords.add(words)
        textFile.close()


def removeStopWords(wordlist):
    '''
    Removes the stopwords from the sentences
    :param wordlist: list of stopwords
    '''
    newlist = []
    for word in wordlist:
        if word not in stopwords:
            newlist.append(word)   
    return newlist
    