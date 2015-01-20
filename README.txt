

### Test environment ###

This package has been tested in a virtual environement (virtualenv) on Python
2.7. Required libraries are specified in requirements.txt They can be installed
with the command ‘pip install -r requirements.txt’

Tests have been run with Nosetests. You can run them from the directory above
‘tests’ with the command ‘nosetests’.

All the modules are PyLint compliant.



### The example script ###

The script named ‘script_that_prints_an_example.py’ will allow you to run your
own examples easily.



### About selecting fragments to be snippets ###

When a keyword is identified in the document, I'm building 3 fragments of the 
documents for scoring. 

1. the keyword is in the middle of the fragment
2. the keyword is at the left edge of the fragment
3. the keyword is at the right edge of the fragment.

This way I'm exhaustively considering all possibly relevant snippets.



### About the scoring of snippets ###

This is the docstring from the scorer module :

'''The scorer computes a relevance score for each fragment given by the
fragmenter and picks the fragment with the highest score

    The score is computed this way :

        (number of matching keyword in the fragment) divided by (number of
        occurences of the keyword in the document)

        Where a keyword is a word in the query.

        In Information Retrieval theory terms  :

            - the numerator is the term frequency of the word in the fragment.
            - the denominator is the collection frequency of the word in the document.
        
        Where the document represents the collection of fragments.

        This scoring gives a higher importance to keywords that are rare in the
        document, over keywords that are frequent in the document. This way the
        influence of common words is smoothed.

        Therefore we can expect the fragment with the higher score to have a
        high number of keywords as well as a variety of them.        


This is the thought process that led me to make this choice.

At first I wanted to do TF-IDF scoring which is very efficient for retrieving
relevant document in a large archive. (en.wikipedia.org/wiki/Tf–idf)

In this case the documents would have been the fragments and the archive the
document. But the parallel breaks because the words in the query are there in
most of the fragments therefore receiving and IDF weight of zero.

That's because fragments are picked as being good candidates to represent the
document and are expected to include the keywords. The document being itself a
good match for the keywords, it is supposed to have a high frequency for the
keywords. Leading these keywords to be there in most fragments if not all, and
in TF-IDF that means that these words are not usefull but they are and we even 
want highlight them.

Another more naive approach would just use the term frequency only, this way the
 ore keywords are in your fragments the better. But if the query contains common
 words such as stop-words they’ll receive a disproportionate importance.

That’s why I decided to smooth their importance by dividing the score of each
word by it’s collection frequency in the document.




### About the running time ###

Length of document: n words 
Length of query: m words
Maximum length of a word: k chars
Number of fragments: f (expected to be small, 3*number of matching
keywords)

I’m analyzing the complexities in the context of the highlight_doc function.


# The tokenizer will run in O(n + m) 

Because we tokenize both the document and the query.


# The fragmenter will run in expected : O(nm) + O(nf)

First loop: O(nmk) in the worst case. Expected O(nm) For each token in the query
and in the document we make a comparison. In the expected case the query word is
rare in the document, therefore most comparisons are done in constant time.

Second loop:  Worst case and expected case O(nf). We loop through the keyword’s
position that have been found in the document, which is also the number of
fragments f. O(f) The extraction of a fragment is done in O(n) because for each
fragment we must go through the document.

expected : O(n(m+f)) worst : O(n(mk+f))


# The scorer will run in expected O(fm)

For each fragment we need ot go through each word in the query : O(fm). We have
to do that many comparisons, most of them will be resolved in O(1) and only few
ones in O(k). When there is a match which expected to be rare we need to go
through the document to to count the occurences for this keyword, this cost
O(n).

expected: O(fmn) worst: O(fmkn)


# The formatter will run in O(m)

For each token representing the best fragment, there is only a limited number
of them O(1) we check if they appear in the query O(m) and perform a few 
constant time operations accordingly.


# The function as whole is expected to run in O(nm)

The worst case scenario is encoutered with a document and a query that matches
it's every word. In that case the fragmenter which would be O(n^2) will
immediately become a bottle neck.

A scenario that is more likely to happen and which would be very expensive to
run would be a long document with a long query and a lot of common words between
them.

However in our use case we can imagine limiting the length of the query as well
as not referencing poorly written documents that are made of only a few words
repeated over and over.





