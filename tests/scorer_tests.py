'''Tests for the scorer module'''


from nose.tools import assert_equal
import snippet_highlighter.scorer


def test_scorer_document_smaller_than_MAX_CHARS():

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

    fragments = ['chicken toast tomato']

    list_of_best_fragment_tokens = snippet_highlighter.scorer.scorer(fragments, list_of_doc_tokens, list_of_query_tokens)[0]
    max_score = snippet_highlighter.scorer.scorer(fragments, list_of_doc_tokens, list_of_query_tokens)[1]

    assert max_score > 0
    # 'chicken' being the first word of the document and in the query, it must be in first position of the list of tokens that represent the best fragment
    assert 'chicken' in list_of_best_fragment_tokens[0]['original_word']


def test_scorer_document_smaller_than_MAX_CHARS_query_not_there():
    # This time the query word is not in the document.
    # In that case the scorer will return a fragment anyway which allows the other functions to keep going.

    # Defining the test query
    token = {}
    token['original_word'] = 'eggs'
    token['tokenized_word'] = 'egg'
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

    fragments = ['chicken toast tomato']

    list_of_best_fragment_tokens = snippet_highlighter.scorer.scorer(fragments, list_of_doc_tokens, list_of_query_tokens)[0]
    max_score = snippet_highlighter.scorer.scorer(fragments, list_of_doc_tokens, list_of_query_tokens)[1]

    assert max_score == 0
    assert list_of_best_fragment_tokens == list_of_doc_tokens # In this case the only fragment and the doc are the same.





# Testing the scorer on doc that are longer than MAX_CHARS

doc = "Continuing on my Saturday morning hangover theme: there's just something about a plateful of greasy food when you're slightly hung over that makes it all better. The Pine Cone has down-home, rib-sticking, greasy food in spades.  The SO and I split the chicken fried steak, which comes with plenty of toast, hashbrowns, and two eggs.  I could'nt finish mine!  The gravy must be the same that they use for biscuits and gravy, because it tasted sausage-y, and as my plate sat there I could see the grease rising to the top.  BUT--I didn't come here in search of health food, and it was just what the doctor ordered chicken . I'll work out later."
list_of_doc_tokens = [{'original_position': 0, 'tokenized_word': 'continu', 'original_word': 'Continuing'}, {'original_position': 11, 'tokenized_word': 'on', 'original_word': 'on'}, {'original_position': 14, 'tokenized_word': 'my', 'original_word': 'my'}, {'original_position': 17, 'tokenized_word': 'saturday', 'original_word': 'Saturday'}, {'original_position': 26, 'tokenized_word': 'morn', 'original_word': 'morning'}, {'original_position': 34, 'tokenized_word': 'hangov', 'original_word': 'hangover'}, {'original_position': 43, 'tokenized_word': 'theme', 'original_word': 'theme:'}, {'original_position': 50, 'tokenized_word': 'there', 'original_word': "there's"}, {'original_position': 58, 'tokenized_word': 'just', 'original_word': 'just'}, {'original_position': 63, 'tokenized_word': 'someth', 'original_word': 'something'}, {'original_position': 73, 'tokenized_word': 'about', 'original_word': 'about'}, {'original_position': 79, 'tokenized_word': 'a', 'original_word': 'a'}, {'original_position': 81, 'tokenized_word': 'plate', 'original_word': 'plateful'}, {'original_position': 90, 'tokenized_word': 'of', 'original_word': 'of'}, {'original_position': 93, 'tokenized_word': 'greasi', 'original_word': 'greasy'}, {'original_position': 100, 'tokenized_word': 'food', 'original_word': 'food'}, {'original_position': 105, 'tokenized_word': 'when', 'original_word': 'when'}, {'original_position': 110, 'tokenized_word': 'your', 'original_word': "you're"}, {'original_position': 117, 'tokenized_word': 'slight', 'original_word': 'slightly'}, {'original_position': 126, 'tokenized_word': 'hung', 'original_word': 'hung'}, {'original_position': 131, 'tokenized_word': 'over', 'original_word': 'over'}, {'original_position': 136, 'tokenized_word': 'that', 'original_word': 'that'}, {'original_position': 141, 'tokenized_word': 'make', 'original_word': 'makes'}, {'original_position': 147, 'tokenized_word': 'it', 'original_word': 'it'}, {'original_position': 150, 'tokenized_word': 'all', 'original_word': 'all'}, {'original_position': 154, 'tokenized_word': 'better', 'original_word': 'better.'}, {'original_position': 162, 'tokenized_word': 'the', 'original_word': 'The'}, {'original_position': 166, 'tokenized_word': 'pine', 'original_word': 'Pine'}, {'original_position': 171, 'tokenized_word': 'cone', 'original_word': 'Cone'}, {'original_position': 176, 'tokenized_word': 'has', 'original_word': 'has'}, {'original_position': 180, 'tokenized_word': 'downhom', 'original_word': 'down-home,'}, {'original_position': 191, 'tokenized_word': 'ribstick', 'original_word': 'rib-sticking,'}, {'original_position': 205, 'tokenized_word': 'greasi', 'original_word': 'greasy'}, {'original_position': 212, 'tokenized_word': 'food', 'original_word': 'food'}, {'original_position': 217, 'tokenized_word': 'in', 'original_word': 'in'}, {'original_position': 220, 'tokenized_word': 'spade', 'original_word': 'spades.'}, {'original_position': 228, 'tokenized_word': '', 'original_word': ''}, {'original_position': 229, 'tokenized_word': 'the', 'original_word': 'The'}, {'original_position': 233, 'tokenized_word': 'so', 'original_word': 'SO'}, {'original_position': 236, 'tokenized_word': 'and', 'original_word': 'and'}, {'original_position': 240, 'tokenized_word': 'i', 'original_word': 'I'}, {'original_position': 242, 'tokenized_word': 'split', 'original_word': 'split'}, {'original_position': 248, 'tokenized_word': 'the', 'original_word': 'the'}, {'original_position': 252, 'tokenized_word': 'chicken', 'original_word': 'chicken'}, {'original_position': 260, 'tokenized_word': 'fri', 'original_word': 'fried'}, {'original_position': 266, 'tokenized_word': 'steak', 'original_word': 'steak,'}, {'original_position': 273, 'tokenized_word': 'which', 'original_word': 'which'}, {'original_position': 279, 'tokenized_word': 'come', 'original_word': 'comes'}, {'original_position': 285, 'tokenized_word': 'with', 'original_word': 'with'}, {'original_position': 290, 'tokenized_word': 'plenti', 'original_word': 'plenty'}, {'original_position': 297, 'tokenized_word': 'of', 'original_word': 'of'}, {'original_position': 300, 'tokenized_word': 'toast', 'original_word': 'toast,'}, {'original_position': 307, 'tokenized_word': 'hashbrown', 'original_word': 'hashbrowns,'}, {'original_position': 319, 'tokenized_word': 'and', 'original_word': 'and'}, {'original_position': 323, 'tokenized_word': 'two', 'original_word': 'two'}, {'original_position': 327, 'tokenized_word': 'egg', 'original_word': 'eggs.'}, {'original_position': 333, 'tokenized_word': '', 'original_word': ''}, {'original_position': 334, 'tokenized_word': 'i', 'original_word': 'I'}, {'original_position': 336, 'tokenized_word': 'couldnt', 'original_word': "could'nt"}, {'original_position': 345, 'tokenized_word': 'finish', 'original_word': 'finish'}, {'original_position': 352, 'tokenized_word': 'mine', 'original_word': 'mine!'}, {'original_position': 358, 'tokenized_word': '', 'original_word': ''}, {'original_position': 359, 'tokenized_word': 'the', 'original_word': 'The'}, {'original_position': 363, 'tokenized_word': 'gravi', 'original_word': 'gravy'}, {'original_position': 369, 'tokenized_word': 'must', 'original_word': 'must'}, {'original_position': 374, 'tokenized_word': 'be', 'original_word': 'be'}, {'original_position': 377, 'tokenized_word': 'the', 'original_word': 'the'}, {'original_position': 381, 'tokenized_word': 'same', 'original_word': 'same'}, {'original_position': 386, 'tokenized_word': 'that', 'original_word': 'that'}, {'original_position': 391, 'tokenized_word': 'they', 'original_word': 'they'}, {'original_position': 396, 'tokenized_word': 'use', 'original_word': 'use'}, {'original_position': 400, 'tokenized_word': 'for', 'original_word': 'for'}, {'original_position': 404, 'tokenized_word': 'biscuit', 'original_word': 'biscuits'}, {'original_position': 413, 'tokenized_word': 'and', 'original_word': 'and'}, {'original_position': 417, 'tokenized_word': 'gravi', 'original_word': 'gravy,'}, {'original_position': 424, 'tokenized_word': 'becaus', 'original_word': 'because'}, {'original_position': 432, 'tokenized_word': 'it', 'original_word': 'it'}, {'original_position': 435, 'tokenized_word': 'tast', 'original_word': 'tasted'}, {'original_position': 442, 'tokenized_word': 'sausagey', 'original_word': 'sausage-y,'}, {'original_position': 453, 'tokenized_word': 'and', 'original_word': 'and'}, {'original_position': 457, 'tokenized_word': 'as', 'original_word': 'as'}, {'original_position': 460, 'tokenized_word': 'my', 'original_word': 'my'}, {'original_position': 463, 'tokenized_word': 'plate', 'original_word': 'plate'}, {'original_position': 469, 'tokenized_word': 'sat', 'original_word': 'sat'}, {'original_position': 473, 'tokenized_word': 'there', 'original_word': 'there'}, {'original_position': 479, 'tokenized_word': 'i', 'original_word': 'I'}, {'original_position': 481, 'tokenized_word': 'could', 'original_word': 'could'}, {'original_position': 487, 'tokenized_word': 'see', 'original_word': 'see'}, {'original_position': 491, 'tokenized_word': 'the', 'original_word': 'the'}, {'original_position': 495, 'tokenized_word': 'greas', 'original_word': 'grease'}, {'original_position': 502, 'tokenized_word': 'rise', 'original_word': 'rising'}, {'original_position': 509, 'tokenized_word': 'to', 'original_word': 'to'}, {'original_position': 512, 'tokenized_word': 'the', 'original_word': 'the'}, {'original_position': 516, 'tokenized_word': 'top', 'original_word': 'top.'}, {'original_position': 521, 'tokenized_word': '', 'original_word': ''}, {'original_position': 522, 'tokenized_word': 'buti', 'original_word': 'BUT--I'}, {'original_position': 529, 'tokenized_word': 'didnt', 'original_word': "didn't"}, {'original_position': 536, 'tokenized_word': 'come', 'original_word': 'come'}, {'original_position': 541, 'tokenized_word': 'here', 'original_word': 'here'}, {'original_position': 546, 'tokenized_word': 'in', 'original_word': 'in'}, {'original_position': 549, 'tokenized_word': 'search', 'original_word': 'search'}, {'original_position': 556, 'tokenized_word': 'of', 'original_word': 'of'}, {'original_position': 559, 'tokenized_word': 'health', 'original_word': 'health'}, {'original_position': 566, 'tokenized_word': 'food', 'original_word': 'food,'}, {'original_position': 572, 'tokenized_word': 'and', 'original_word': 'and'}, {'original_position': 576, 'tokenized_word': 'it', 'original_word': 'it'}, {'original_position': 579, 'tokenized_word': 'was', 'original_word': 'was'}, {'original_position': 583, 'tokenized_word': 'just', 'original_word': 'just'}, {'original_position': 588, 'tokenized_word': 'what', 'original_word': 'what'}, {'original_position': 593, 'tokenized_word': 'the', 'original_word': 'the'}, {'original_position': 597, 'tokenized_word': 'doctor', 'original_word': 'doctor'}, {'original_position': 604, 'tokenized_word': 'order', 'original_word': 'ordered'}, {'original_position': 612, 'tokenized_word': 'chicken', 'original_word': 'chicken'}, {'original_position': 620, 'tokenized_word': '', 'original_word': '.'}, {'original_position': 622, 'tokenized_word': 'ill', 'original_word': "I'll"}, {'original_position': 627, 'tokenized_word': 'work', 'original_word': 'work'}, {'original_position': 632, 'tokenized_word': 'out', 'original_word': 'out'}, {'original_position': 636, 'tokenized_word': 'later', 'original_word': 'later.'}]


def test_scorer_single_word_in_query_more_than_MAX_CHARS():

    query = 'Saturday'
    list_of_query_tokens = [{'original_position': 0, 'tokenized_word': 'saturday', 'original_word': 'Saturday'}]

    fragments = ["Continuing on my Saturday morning hangover theme: there's just something about a plateful of greasy food when you're", "Saturday morning hangover theme: there's just something about a plateful of greasy food when you're slightly hung over that makes it all better. The Pine Cone has down-home, rib-sticking, greasy food", 'Continuing on my Saturday']
    expected_list_of_best_fragment_tokens = [{'original_position': 0, 'tokenized_word': 'continu', 'original_word': 'Continuing'}, {'original_position': 11, 'tokenized_word': 'on', 'original_word': 'on'}, {'original_position': 14, 'tokenized_word': 'my', 'original_word': 'my'}, {'original_position': 17, 'tokenized_word': 'saturday', 'original_word': 'Saturday'}, {'original_position': 26, 'tokenized_word': 'morn', 'original_word': 'morning'}, {'original_position': 34, 'tokenized_word': 'hangov', 'original_word': 'hangover'}, {'original_position': 43, 'tokenized_word': 'theme', 'original_word': 'theme:'}, {'original_position': 50, 'tokenized_word': 'there', 'original_word': "there's"}, {'original_position': 58, 'tokenized_word': 'just', 'original_word': 'just'}, {'original_position': 63, 'tokenized_word': 'someth', 'original_word': 'something'}, {'original_position': 73, 'tokenized_word': 'about', 'original_word': 'about'}, {'original_position': 79, 'tokenized_word': 'a', 'original_word': 'a'}, {'original_position': 81, 'tokenized_word': 'plate', 'original_word': 'plateful'}, {'original_position': 90, 'tokenized_word': 'of', 'original_word': 'of'}, {'original_position': 93, 'tokenized_word': 'greasi', 'original_word': 'greasy'}, {'original_position': 100, 'tokenized_word': 'food', 'original_word': 'food'}, {'original_position': 105, 'tokenized_word': 'when', 'original_word': 'when'}, {'original_position': 110, 'tokenized_word': 'your', 'original_word': "you're"}]

    list_of_best_fragment_tokens = snippet_highlighter.scorer.scorer(fragments, list_of_doc_tokens, list_of_query_tokens)[0]
    max_score = snippet_highlighter.scorer.scorer(fragments, list_of_doc_tokens, list_of_query_tokens)[1]

    # Saturday is in the document only once, therefore all fragments will have the same score of 1
    # And the first fragment will be returned as the best one.

    assert_equal(max_score, 1.0)
    assert_equal(list_of_best_fragment_tokens, expected_list_of_best_fragment_tokens)


def test_scorer_several_words_in_query_more_than_MAX_CHARS():

    query = 'Saturday greasy' # In this case 'eggs' is immediately followed by a dot in the document.
    list_of_query_tokens = [{'original_position': 0, 'tokenized_word': 'saturday', 'original_word': 'Saturday'}, {'original_position': 9, 'tokenized_word': 'greasi', 'original_word': 'greasy'}]

    fragments = ["Continuing on my Saturday morning hangover theme: there's just something about a plateful of greasy food when you're", "Saturday morning hangover theme: there's just something about a plateful of greasy food when you're slightly hung over that makes it all better. The Pine Cone has down-home, rib-sticking, greasy food", 'Continuing on my Saturday', "Continuing on my Saturday morning hangover theme: there's just something about a plateful of greasy food when you're slightly hung over that makes it all better. The Pine Cone has down-home, ri", "greasy food when you're slightly hung over that makes it all better. The Pine Cone has down-home, rib-sticking, greasy food in spades.  The SO and I split the chicken fried steak, which comes with ple", "Continuing on my Saturday morning hangover theme: there's just something about a plateful of greasy", "when you're slightly hung over that makes it all better. The Pine Cone has down-home, rib-sticking, greasy food in spades.  The SO and I split the chicken fried steak, which comes with plenty of toast", "greasy food in spades.  The SO and I split the chicken fried steak, which comes with plenty of toast, hashbrowns, and two eggs.  I could'nt finish mine!  The gravy must be the same that they use for b", "on my Saturday morning hangover theme: there's just something about a plateful of greasy food when you're slightly hung over that makes it all better. The Pine Cone has down-home, rib-sticking, greasy"]
    expected_list_of_best_fragment_tokens = [{'original_position': 0, 'tokenized_word': 'saturday', 'original_word': 'Saturday'}, {'original_position': 9, 'tokenized_word': 'morn', 'original_word': 'morning'}, {'original_position': 17, 'tokenized_word': 'hangov', 'original_word': 'hangover'}, {'original_position': 26, 'tokenized_word': 'theme', 'original_word': 'theme:'}, {'original_position': 33, 'tokenized_word': 'there', 'original_word': "there's"}, {'original_position': 41, 'tokenized_word': 'just', 'original_word': 'just'}, {'original_position': 46, 'tokenized_word': 'someth', 'original_word': 'something'}, {'original_position': 56, 'tokenized_word': 'about', 'original_word': 'about'}, {'original_position': 62, 'tokenized_word': 'a', 'original_word': 'a'}, {'original_position': 64, 'tokenized_word': 'plate', 'original_word': 'plateful'}, {'original_position': 73, 'tokenized_word': 'of', 'original_word': 'of'}, {'original_position': 76, 'tokenized_word': 'greasi', 'original_word': 'greasy'}, {'original_position': 83, 'tokenized_word': 'food', 'original_word': 'food'}, {'original_position': 88, 'tokenized_word': 'when', 'original_word': 'when'}, {'original_position': 93, 'tokenized_word': 'your', 'original_word': "you're"}, {'original_position': 100, 'tokenized_word': 'slight', 'original_word': 'slightly'}, {'original_position': 109, 'tokenized_word': 'hung', 'original_word': 'hung'}, {'original_position': 114, 'tokenized_word': 'over', 'original_word': 'over'}, {'original_position': 119, 'tokenized_word': 'that', 'original_word': 'that'}, {'original_position': 124, 'tokenized_word': 'make', 'original_word': 'makes'}, {'original_position': 130, 'tokenized_word': 'it', 'original_word': 'it'}, {'original_position': 133, 'tokenized_word': 'all', 'original_word': 'all'}, {'original_position': 137, 'tokenized_word': 'better', 'original_word': 'better.'}, {'original_position': 145, 'tokenized_word': 'the', 'original_word': 'The'}, {'original_position': 149, 'tokenized_word': 'pine', 'original_word': 'Pine'}, {'original_position': 154, 'tokenized_word': 'cone', 'original_word': 'Cone'}, {'original_position': 159, 'tokenized_word': 'has', 'original_word': 'has'}, {'original_position': 163, 'tokenized_word': 'downhom', 'original_word': 'down-home,'}, {'original_position': 174, 'tokenized_word': 'ribstick', 'original_word': 'rib-sticking,'}, {'original_position': 188, 'tokenized_word': 'greasi', 'original_word': 'greasy'}, {'original_position': 195, 'tokenized_word': 'food', 'original_word': 'food'}]

    list_of_best_fragment_tokens = snippet_highlighter.scorer.scorer(fragments, list_of_doc_tokens, list_of_query_tokens)[0]
    max_score = snippet_highlighter.scorer.scorer(fragments, list_of_doc_tokens, list_of_query_tokens)[1]

    assert_equal(max_score, 2.0)
    assert_equal(list_of_best_fragment_tokens, expected_list_of_best_fragment_tokens)
