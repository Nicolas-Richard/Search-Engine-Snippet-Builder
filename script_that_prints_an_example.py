''' This script allows you to test the highlight_doc function by printing what's happening at every step
This script should be run in the top level directory
'''

from snippet_highlighter.tokenizer import tokenizer
from snippet_highlighter.fragmenter import fragmenter
from snippet_highlighter.scorer import scorer
from snippet_highlighter.formatter import formatter


# From an actual review
doc = "Continuing on my Saturday morning hangover theme: there's just something about a plateful of greasy food when you're slightly hung over that makes it all better. The Pine Cone has down-home, rib-sticking, greasy food in spades.  The SO and I split the chicken fried steak, which comes with plenty of toast, hashbrowns, and two eggs.  I could'nt finish mine!  The gravy must be the same that they use for biscuits and gravy, because it tasted sausage-y, and as my plate sat there I could see the grease rising to the top.  BUT--I didn't come here in search of health food, and it was just what the doctor ordered chicken . I'll work out later."
query = ' hashbrowns eggs'

# Trivial doc & query
#doc = 'chicken toast tomato'
#query = 'chicken'

# For your own examples
#doc = raw_input('Enter your doc: ')
#query = raw_input('Enter your query: ')


def enjoy_highlight_doc():


    # 1. We tokenize the documents and the query
    list_of_doc_tokens = tokenizer(doc)
    list_of_query_tokens = tokenizer(query)
    #print list_of_doc_tokens
    #print list_of_query_tokens
    #print '-'*25

    # 2. We fragment the document
    fragments = fragmenter(list_of_doc_tokens, list_of_query_tokens)
    #print fragments
    #print '-'*25

    # 3. We score each fragment and pick the most relevant one
    list_of_best_fragment_tokens = scorer(fragments, list_of_doc_tokens, list_of_query_tokens)[0]    
    max_score = scorer(fragments, list_of_doc_tokens, list_of_query_tokens)[1]
    # In the scorer function you can uncomment 'print score' to print the score of each fragment
    #print list_of_best_fragment_tokens
    #print max_score
    #print '-'*25

    # 4. We format the most relevant fragment and return it
    snippet = formatter(list_of_best_fragment_tokens, list_of_query_tokens)
    print snippet

    return snippet

enjoy_highlight_doc()	
