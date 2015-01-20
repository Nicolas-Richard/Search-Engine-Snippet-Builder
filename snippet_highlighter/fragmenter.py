'''Given a query the fragmenter builds snippets candidates from the document for
the scorer function.'''

from snippet_highlighter.tokenizer import build_doc_from_tokens

MAX_CHARS = 200

def fragmenter(list_of_doc_tokens, list_of_query_tokens):
    """Looks for matched terms and aggregates them with their surrounding
    context.
    Args:
        list_of_doc_tokens -- The tokens for the document to be fragmented (list of dict)
        list_of_query_tokens -- The query for the search string (list of dict)

    Returns:
        fragments -- extracts of the document where the query words are present (list of strings)
    """

    doc = build_doc_from_tokens(list_of_doc_tokens, False) # When False is specified the original
                                                           # words are used to build the document

    if len(doc) < MAX_CHARS:
        return [doc]


    fragments = []
    keyword_start_position = []

    query_token = list_of_query_tokens[0]

    for query_token in list_of_query_tokens:
        for doc_token in list_of_doc_tokens:

            if query_token['tokenized_word'] == doc_token['tokenized_word']:
                keyword_start_position.append((doc_token['original_position'],
                                               doc_token['original_word']))

    if keyword_start_position == []: # This happens if none of the words in the query is found in
                                     # the document, I return the 200 first chars in the document
        return [doc[200:]]

    #print keyword_start_position
    for i in range(len(keyword_start_position)):
        fragments.append(extract_fragment(doc, keyword_start_position[i][0], True, True))
        fragments.append(extract_fragment(doc, keyword_start_position[i][0] + MAX_CHARS/2, False,
                                          True))
        fragments.append(extract_fragment(doc, keyword_start_position[i][0] +
                                          len(keyword_start_position[i][1]) - MAX_CHARS/2, True,
                                          False))

    return fragments

def extract_fragment(doc, index, left_flag, right_flag):
    """Cleanly extract the text surrounding the word in position index in the string doc.
    No words will be sliced at the edges of the string and punctuation (...) will be added if
    needed.
    Args:
        doc -- string to extract from (string)
        index -- position of the first letter of the word defining the extraction (int)
        left_flag -- the left end must be cleaned (boolean)
        right_flag -- the right end must be cleaned (boolean)

    Returns:
        fragment -- string containing the word to be extracted and it's surrounding context
        (string)
    """

    left_cut = max(index - MAX_CHARS/2, 0)
    right_cut = min(index + MAX_CHARS/2, len(doc))

    # Special care for edge cases (when we bump against the edge of the document)

    if left_cut == 0:
        left_flag = False
    if  right_cut == len(doc):
        right_flag = False

    # Let's take care of the left edge first.

    left_punctuation_flag = False # This flag will let us know if we have space to add '... '
    if left_flag and doc[left_cut-1].isalnum() and doc[left_cut].isalnum(): # I'm scling a word
        # Let's find how much I need to clean
        i = left_cut
        while doc[i] != ' ':
            i += 1
        if i - left_cut >= 4:
            left_punctuation_flag = True
        left_cut = i
        left_flag = False
    else:
        left_flag = False

    # Let's take care of the right edge now.

    right_punctuation_flag = False # This flag will let us know if we have space to add ' ...'
    if right_flag and doc[right_cut].isalnum() and doc[right_cut-1].isalnum(): #I'm slicing a word
        # Let's find how much I need to clean
        j = right_cut
        while doc[j] != ' ':
            j -= 1
        if right_cut - j >= 4:
            right_punctuation_flag = True
        right_cut = j
        right_flag = False
    else:
        right_flag = False

    fragment = (doc[left_cut:right_cut]).strip()

    # At this point we have a fragment with a first and last words that have been nicely cut
    # If needed and if possible I'm going to add '...' marks at the edges of the fragment

    if left_punctuation_flag == True:
        fragment = "".join(['... ', fragment])
        left_punctuation_flag = False
    if right_punctuation_flag == True:
        fragment = "".join([fragment, ' ...'])
        right_punctuation_flag = False

    return fragment
