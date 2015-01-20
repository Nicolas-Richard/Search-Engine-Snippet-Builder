'''The formatter inserts tags around the query words found in a fragment'''

from snippet_highlighter.tokenizer import build_doc_from_tokens


def formatter(list_of_best_fragment_tokens, list_of_query_tokens):
    '''Returns a formatted version of the given fragment where the query
    words are highlighted
    Args:
        list_of_best_fragment_tokens -- The query for the best fragment (list of dict)
        list_of_query_tokens -- The query for the search string (list of dict)
    Returns:
        highlighted_snippet -- string with the matching words from the query highlighted
    '''

    highlighted_snippet = ''

    tokenized_query = build_doc_from_tokens(list_of_query_tokens)

    for fragment_token in list_of_best_fragment_tokens:

        if fragment_token['tokenized_word'] in tokenized_query.split():
        # Above, need to use split otherwise any substring would match.
        # Ex: 'the' will matche in 'therefore'

            highlighted_snippet = ' '.join([highlighted_snippet, '[[HIGHLIGHT]]'])
            highlighted_snippet = ''.join([highlighted_snippet, fragment_token['original_word']])
            highlighted_snippet = ''.join([highlighted_snippet, '[[ENDHIGHLIGHT]]'])

        else:
            highlighted_snippet = ' '.join([highlighted_snippet, fragment_token['original_word']])

    return highlighted_snippet.replace('[[ENDHIGHLIGHT]] [[HIGHLIGHT]]', ' ').strip()
