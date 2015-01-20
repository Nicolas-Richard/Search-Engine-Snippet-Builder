'''This is the main function requested in the exercise
Given a document and a query it returns the best possible snippet with
highlighted keywords'''

from snippet_highlighter.tokenizer import tokenizer
from snippet_highlighter.fragmenter import fragmenter
from snippet_highlighter.scorer import scorer
from snippet_highlighter.formatter import formatter

MAX_LENGTH_DOC = 2500
MAX_LENGTH_QUERY = 50

def highlight_doc(doc, query):
    """
    Args:
        doc -- Document to be highlighted (string)
        query -- The search query (string)

    Returns: The most relevant snippet with the query terms highlighted (string)
    """

    if len(doc) > MAX_LENGTH_DOC:
        doc = doc[:MAX_LENGTH_DOC]

    if len(query) > MAX_LENGTH_QUERY:
        query = query[:MAX_LENGTH_QUERY]

    # 1. We tokenize the documents and the query
    list_of_doc_tokens = tokenizer(doc)
    list_of_query_tokens = tokenizer(query)

    # 2. We fragment the document
    fragments = fragmenter(list_of_doc_tokens, list_of_query_tokens)

    # 3. We score each fragment and pick the most relevant one
    list_of_best_fragment_tokens = scorer(fragments, list_of_doc_tokens, list_of_query_tokens)[0]

    # 4. We format the most relevant fragment and return it
    return formatter(list_of_best_fragment_tokens, list_of_query_tokens)


