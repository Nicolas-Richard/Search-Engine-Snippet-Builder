
'''Given a string the tokenizer builds a list of tokens. Words in the doc are separated by a
space, and for each word a token is created. Each token includes the original_word, the
tokenized_word (lower case, stemmed and without punctuation version of the word) and the
original_position of the word in the string.
'''

import string
from stemming.porter2 import stem


def tokenizer(doc):
    """Builds a list of tokens from the words in the document
    Args:
        doc -- document to be tokenized (string)

    Returns:
        list_of_tokens -- the list of tokens built from the document. One token for every word.
        (list of dicts)
    """

    doc = doc.strip() # Heading and trailing spaces have no value here
    exclude = set(string.punctuation) # Let's prepare to get rid off punctuation
    splitted_doc = doc.split(' ')
    list_of_tokens = []

    for i in range(len(splitted_doc)):

        token = {} # Each token is dictionnary
        token['original_word'] = splitted_doc[i]
        token['tokenized_word'] = stem(''.join(ch for ch in splitted_doc[i]
        							  if ch not in exclude).lower())
        token['original_position'] = len(' '.join(splitted_doc[:i+1])) - len(splitted_doc[i])

        list_of_tokens.append(token)

    return list_of_tokens


def build_doc_from_tokens(list_of_tokens, tokenized=True):
    """Puts together a document from a list of tokens.
    Args:
        list_of_tokens -- list of tokens given by the tokenizer (list of dicts)
        tokenized -- True (default) for the words in their tokenized form. False for the original
        words (boolean)

    Returns:
        result -- a string made of the tokenized words in the tokens (string)
    """

    result = ''

    if tokenized == True:

        for i in range(len(list_of_tokens)):
            result = ' '.join([result, list_of_tokens[i]['tokenized_word']])

        return result.strip()

    else:

        for i in range(len(list_of_tokens)):
            result = ' '.join([result, list_of_tokens[i]['original_word']])

        return result.strip()




