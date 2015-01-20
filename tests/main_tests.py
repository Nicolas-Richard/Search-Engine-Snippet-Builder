from nose.tools import *
import snippet_highlighter.main


# Test the highlight_doc function

def test_highlight_doc_query1():

	doc = "Continuing on my Saturday morning hangover theme: there's just something about a plateful of greasy food when you're slightly hung over that makes it all better. The Pine Cone has down-home, rib-sticking, greasy food in spades.  The SO and I split the chicken fried steak, which comes with plenty of toast, hashbrowns, and two eggs.  I could'nt finish mine!  The gravy must be the same that they use for biscuits and gravy, because it tasted sausage-y, and as my plate sat there I could see the grease rising to the top.  BUT--I didn't come here in search of health food, and it was just what the doctor ordered chicken . I'll work out later."
	query1 = 'greasy hashbrowns toasts eggs'

	snippet = snippet_highlighter.main.highlight_doc(doc,query1)

	expected = "[[HIGHLIGHT]]greasy[[ENDHIGHLIGHT]] food in spades.  The SO and I split the chicken fried steak, which comes with plenty of [[HIGHLIGHT]]toast, hashbrowns,[[ENDHIGHLIGHT]] and two [[HIGHLIGHT]]eggs.[[ENDHIGHLIGHT]]  I could'nt finish mine!  The gravy must be the same that they use for"

	assert_equal(snippet,expected)

def test_highlight_doc_query2():

	doc = "Continuing on my Saturday morning hangover theme: there's just something about a plateful of greasy food when you're slightly hung over that makes it all better. The Pine Cone has down-home, rib-sticking, greasy food in spades.  The SO and I split the chicken fried steak, which comes with plenty of toast, hashbrowns, and two eggs.  I could'nt finish mine!  The gravy must be the same that they use for biscuits and gravy, because it tasted sausage-y, and as my plate sat there I could see the grease rising to the top.  BUT--I didn't come here in search of health food, and it was just what the doctor ordered chicken . I'll work out later."
	query2 = 'chicken fried biscuits'

	snippet = snippet_highlighter.main.highlight_doc(doc,query2)

	expected = "[[HIGHLIGHT]]chicken fried[[ENDHIGHLIGHT]] steak, which comes with plenty of toast, hashbrowns, and two eggs.  I could'nt finish mine!  The gravy must be the same that they use for [[HIGHLIGHT]]biscuits[[ENDHIGHLIGHT]] and gravy, because it tasted sausage-y,"
	assert_equal(snippet,expected)

def test_highlight_doc_void_query():

	doc = "Continuing on my Saturday morning hangover theme: there's just something about a plateful of greasy food when you're slightly hung over that makes it all better. The Pine Cone has down-home, rib-sticking, greasy food in spades.  The SO and I split the chicken fried steak, which comes with plenty of toast, hashbrowns, and two eggs.  I could'nt finish mine!  The gravy must be the same that they use for biscuits and gravy, because it tasted sausage-y, and as my plate sat there I could see the grease rising to the top.  BUT--I didn't come here in search of health food, and it was just what the doctor ordered chicken . I'll work out later."
	query = ''

	snippet = snippet_highlighter.main.highlight_doc(doc,query)

	assert snippet != ''
	assert len(snippet) <=200

def test_highlight_doc_void_doc():

	doc = ""	
	query = 'chicken'

	snippet = snippet_highlighter.main.highlight_doc(doc,query)

	assert_equal(snippet, '')







