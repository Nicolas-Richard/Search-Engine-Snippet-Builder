'''The scorer computes a relevance score for each fragment given by the
fragmenter and picks the fragment with the highest score

    The score is computed this way :

        (number of matching keyword in the fragment) divided by (number of occurences
        of the keyword in the document)

        Where a keyword is a word in the query.

        In Information Retrieval theory terms  :

            - the numerator is the term frequency of the word in the fragment.
            - the denominator is the collection frequency of the word in the document.
            Where the document represents the collection of fragments.

        This scoring gives a higher importance to keywords that are rare in the document,
        over keywords that are frequent in the document. This way the influence of common words
        is smoothed.

        Therefore we can expect the fragment with the higher score to have a high number of
        keywords as well as a variety of them.

'''

from snippet_highlighter.tokenizer import tokenizer

def scorer(fragments, list_of_doc_tokens, list_of_query_tokens):
    """Give a score to each fragment.
    Args:
        fragments -- list of strings given by the fragmenter
        list_of_doc_tokens -- The tokens for the document to be fragmented (list of dict)
        list_of_query_tokens -- The query for the search string (list of dict)

    Returns:
        list_of_best_fragment_tokens -- The query for the best fragment (list of dict)
    """

    max_score = -1 # Negative for testing purposes.

    for fragment in fragments:

        list_of_fragment_tokens = tokenizer(fragment)

        score = 0
        for query_token in list_of_query_tokens:

            for fragment_token in list_of_fragment_tokens: # If there's a match we're going to add
                                                 # this word's score to the score of this fragment

                if query_token['tokenized_word'] == fragment_token['tokenized_word']:

                    # build doc_count
                    doc_count = 0
                    for doc_token in list_of_doc_tokens:
                        if doc_token['tokenized_word'] == query_token['tokenized_word']:
                            doc_count += 1

                    score += 1./doc_count
                    # flag_document_ok = True

        #print score
        if score > max_score:
            max_score = score
            list_of_best_fragment_tokens = list_of_fragment_tokens


    return (list_of_best_fragment_tokens, max_score) # I keep track of the max_score for testing
