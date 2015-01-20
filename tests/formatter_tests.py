'''Tests for the formatter module'''

from nose.tools import assert_equal
import snippet_highlighter.formatter


def test_formatter_single_single():

    # Defining the test query
    token = {}
    token['original_word'] = 'chicken'
    token['tokenized_word'] = 'chicken'
    token['original_position'] = 0
    list_of_query_tokens = [token]

    # Defining the test doc
    token = {}
    token['original_word'] = 'Chickens' # Here the document and the query are not
                                                                 # an exact match
    token['tokenized_word'] = 'chicken'
    token['original_position'] = 0
    list_of_doc_tokens = [token]

    expected_snippet = '[[HIGHLIGHT]]Chickens[[ENDHIGHLIGHT]]'
    actual_snippet = snippet_highlighter.formatter.formatter(list_of_doc_tokens,
                                                             list_of_query_tokens)

    assert_equal(expected_snippet, actual_snippet)


def test_formatter_single_several():

    # Defining the test query
    token = {}
    token['original_word'] = 'chicken'
    token['tokenized_word'] = 'chicken'
    token['original_position'] = 0
    list_of_query_tokens = [token]

    # Defining the test document
    list_of_doc_tokens = []

    token1 = {}
    token1['original_word'] = 'chicken'
    token1['tokenized_word'] = 'chicken'
    token1['original_position'] = 0

    token2 = {}
    token2['original_word'] = 'toast'
    token2['tokenized_word'] = 'toast'
    token2['original_position'] = 8

    token3 = {}
    token3['original_word'] = 'tomato'
    token3['tokenized_word'] = 'tomato'
    token3['original_position'] = 14

    list_of_doc_tokens.append(token1)
    list_of_doc_tokens.append(token2)
    list_of_doc_tokens.append(token3)

    expected_snippet = '[[HIGHLIGHT]]chicken[[ENDHIGHLIGHT]] toast tomato'
    actual_snippet = snippet_highlighter.formatter.formatter(list_of_doc_tokens,
                                                             list_of_query_tokens)

    assert_equal(expected_snippet, actual_snippet)


def test_formatter_several_several():

    # Defining the test query
    list_of_query_tokens = []

    token1 = {}
    token1['original_word'] = 'chicken'
    token1['tokenized_word'] = 'chicken'
    token1['original_position'] = 0

    token2 = {}
    token2['original_word'] = 'toast'
    token2['tokenized_word'] = 'toast'
    token2['original_position'] = 8

    list_of_query_tokens.append(token1)
    list_of_query_tokens.append(token2)

    # Defining the test document
    list_of_doc_tokens = []

    token1 = {}
    token1['original_word'] = 'chicken'
    token1['tokenized_word'] = 'chicken'
    token1['original_position'] = 0

    token2 = {}
    token2['original_word'] = 'toast'
    token2['tokenized_word'] = 'toast'
    token2['original_position'] = 8

    token3 = {}
    token3['original_word'] = 'tomato'
    token3['tokenized_word'] = 'tomato'
    token3['original_position'] = 14

    list_of_doc_tokens.append(token1)
    list_of_doc_tokens.append(token2)
    list_of_doc_tokens.append(token3)

    expected_snippet = '[[HIGHLIGHT]]chicken toast[[ENDHIGHLIGHT]] tomato'
    actual_snippet = snippet_highlighter.formatter.formatter(list_of_doc_tokens,
                                                             list_of_query_tokens)

    assert_equal(expected_snippet, actual_snippet)
