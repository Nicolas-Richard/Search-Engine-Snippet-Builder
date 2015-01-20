''' Tests for the module tokenizer'''


from nose.tools import assert_equal
import snippet_highlighter.tokenizer


# Test the tokenizer function

def test_tokenizer_single_field_by_field():

    token_chicken = snippet_highlighter.tokenizer.tokenizer('chicken')

    token = {}
    token['original_word'] = 'chicken'
    token['tokenized_word'] = 'chicken'
    token['original_position'] = 0

    assert_equal(token_chicken[0]['original_word'], [token][0]['original_word'])
    assert_equal(token_chicken[0]['tokenized_word'], [token][0]['tokenized_word'])
    assert_equal(token_chicken[0]['original_position'], [token][0]['original_position'])

def test_tokenizer_single_as_a_whole():

    token_chicken = snippet_highlighter.tokenizer.tokenizer('chicken')

    token = {}
    token['original_word'] = 'chicken'
    token['tokenized_word'] = 'chicken'
    token['original_position'] = 0

    assert_equal(token_chicken, [token])

def test_tokenizer_void_string():

    token_void = snippet_highlighter.tokenizer.tokenizer('')

    token = {}
    token['original_word'] = ''
    token['tokenized_word'] = ''
    token['original_position'] = 0

    assert_equal(token_void, [token])


def test_tokenizer_several_words():

    tokens = []

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

    tokens.append(token1)
    tokens.append(token2)
    tokens.append(token3)

    list_of_tokens = snippet_highlighter.tokenizer.tokenizer('chicken toast tomato')

    assert_equal(list_of_tokens, tokens)

def test_tokenizer_twice_same_word():

    tokens = []

    token1 = {}
    token1['original_word'] = 'chicken'
    token1['tokenized_word'] = 'chicken'
    token1['original_position'] = 0

    token2 = {}
    token2['original_word'] = 'chicken'
    token2['tokenized_word'] = 'chicken'
    token2['original_position'] = 8

    tokens.append(token1)
    tokens.append(token2)

    list_of_tokens = snippet_highlighter.tokenizer.tokenizer('chicken chicken')
    assert_equal(list_of_tokens, tokens)

def test_stemming_single_word():

    token = {}
    token['original_word'] = 'chickens'
    token['tokenized_word'] = 'chicken'
    token['original_position'] = 0

    snippet = snippet_highlighter.tokenizer.tokenizer('chickens')
    assert_equal(snippet, [token])

def test_stemming_several_words():

    tokens = []

    token1 = {}
    token1['original_word'] = 'continuing'
    token1['tokenized_word'] = 'continu'
    token1['original_position'] = 0

    token2 = {}
    token2['original_word'] = 'fried'
    token2['tokenized_word'] = 'fri'
    token2['original_position'] = 11

    token3 = {}
    token3['original_word'] = 'gravy'
    token3['tokenized_word'] = 'gravi'
    token3['original_position'] = 17

    tokens.append(token1)
    tokens.append(token2)
    tokens.append(token3)

    snippet = snippet_highlighter.tokenizer.tokenizer('continuing fried gravy')
    assert_equal(snippet, tokens)

# Test the casing of words

def test_casing_single_word():

    token = {}
    token['original_word'] = 'ChIcKeNs'
    token['tokenized_word'] = 'chicken'
    token['original_position'] = 0

    snippet = snippet_highlighter.tokenizer.tokenizer('ChIcKeNs')
    assert_equal(snippet, [token])

# Test the punctuation handling

def test_punctuation_single_word():

    token = {}
    token['original_word'] = '?/=chicken...'
    token['tokenized_word'] = 'chicken'
    token['original_position'] = 0

    snippet = snippet_highlighter.tokenizer.tokenizer('?/=chicken...')
    assert_equal(snippet, [token])

# Test the numbers handling

def test_numbers_in_single_word():
    # Numbers are handled just like other words, if the user is looking for a specific
    # price in a review, he should be able to find it.

    token = {}
    token['original_word'] = '1.25$'
    token['tokenized_word'] = '125'
    token['original_position'] = 0

    snippet = snippet_highlighter.tokenizer.tokenizer('1.25$')
    assert_equal(snippet, [token])




# Test the build_tokenized_doc function #

def test_build_doc_from_tokens_single():

    token = {}
    token['original_word'] = 'chicken'
    token['tokenized_word'] = 'chicken'
    token['original_position'] = 0
    list_of_tokens = [token]

    snippet = snippet_highlighter.tokenizer.build_doc_from_tokens(list_of_tokens)
    assert_equal(snippet, 'chicken')

def test_build_doc_from_tokens_empty():

    token = {}
    token['original_word'] = ''
    token['tokenized_word'] = ''
    token['original_position'] = 0
    list_of_tokens = [token]

    snippet = snippet_highlighter.tokenizer.build_doc_from_tokens(list_of_tokens)
    assert_equal(snippet, '')

def test_build_doc_from_tokens_several_words():

    tokens = []

    token1 = {}
    token1['original_word'] = 'Chicken'
    token1['tokenized_word'] = 'chicken'
    token1['original_position'] = 0

    token2 = {}
    token2['original_word'] = 'toasts'
    token2['tokenized_word'] = 'toast'
    token2['original_position'] = 8

    token3 = {}
    token3['original_word'] = 'tomato?'
    token3['tokenized_word'] = 'tomato'
    token3['original_position'] = 14

    tokens.append(token1)
    tokens.append(token2)
    tokens.append(token3)

    snippet = snippet_highlighter.tokenizer.build_doc_from_tokens(tokens)
    assert_equal(snippet, 'chicken toast tomato')

def test_build_doc_from_tokens_several_words_original_words():

    tokens = []

    token1 = {}
    token1['original_word'] = 'Chicken'
    token1['tokenized_word'] = 'chicken'
    token1['original_position'] = 0

    token2 = {}
    token2['original_word'] = 'toasts'
    token2['tokenized_word'] = 'toast'
    token2['original_position'] = 8

    token3 = {}
    token3['original_word'] = 'tomato?'
    token3['tokenized_word'] = 'tomato'
    token3['original_position'] = 14

    tokens.append(token1)
    tokens.append(token2)
    tokens.append(token3)

    snippet = snippet_highlighter.tokenizer.build_doc_from_tokens(tokens, False)
    assert_equal(snippet, 'Chicken toasts tomato?')

