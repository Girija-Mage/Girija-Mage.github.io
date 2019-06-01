stemWords = {}                    #declarations


def stemmerMarathi(words):
    return [removeCase2(removeCase1(word)) for word in words]


def removeCase1(word):
    '''
    :param word: word to be reduced its stem
    :return: stem of the word
    '''
    #word_length = len(word) - 1
   
    #if word_length > 4:
    suffix = "च्या"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "शी"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "चा"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "ची"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "चे"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "हून"
    if word.endswith(suffix):
        return word[:-len(suffix)]

    #if word_length > 3:
    suffix = "नो"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "तो"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "ने"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "नी"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "ही"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "ते"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "या"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "ला"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "ना"
    if word.endswith(suffix):
        return word[:-len(suffix)]
        

    #if word_length > 2:
    suffix = " े"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = " ी"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "स"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "ल"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = " ा"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "त"
    if word.endswith(suffix):
        return word[:-len(suffix)]
      
    return word


def removeCase2(word):
    '''
    :param word:
    :return:
    '''
    global stemWords
    if word in stemWords:
        return stemWords[word]["stem"]
   # word_length = len(word) - 1

   # if word_length > 4:
    suffix = "ल्या"
    if word.endswith(suffix):
        return word[:-len(suffix)]

   # if word_length > 3:
    suffix = "रु"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "डे"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "ती"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = " ान"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = " ीण"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "डा"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "डी"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "गा"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "ला"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "ळा"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "या"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "वा"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "ये"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "वे"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = "ती"
    if word.endswith(suffix):
        return word[:-len(suffix)]

   # if word_length > 2:
    suffix = "अ"
    if word.endswith(suffix):
        return word[:-len(suffix)]
    suffix = " े"
    if word.endswith(suffix):
        return word[:-len(suffix)]
        suffix = "ि "
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ु"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ौ"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ै"
        if word.endswith(suffix):
            return word[:-len(suffix)]

        suffix = " ा"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ी"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ू"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "त"
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

