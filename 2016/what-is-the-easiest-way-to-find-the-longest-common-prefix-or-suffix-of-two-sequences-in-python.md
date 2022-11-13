# What is the easiest way to find the longest common prefix or suffix of two sequences in Python?

	author: Steve Theodore
	written: 2016-01-12
	views: 3558
	upvotes: 0
	quora url: /What-is-the-easiest-way-to-find-the-longest-common-prefix-or-suffix-of-two-sequences-in-Python/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


What?!?! No genexps?

    def common(seq1, seq2):
    	for j, k in zip(seq1, seq2):
    		if j !=k :
    			break
    		yield j
    start = ''.join(common('abcde', 'abzzz') )
    end = ''.join(common('abcdef'[::-1], 'abzzzef'[::-1]) )
    print start, end

Won't matter 99% of the time but using a generator you don't need to exhaust the common prefix: you can step through it iteratively. I've string joined them but you could list-comprehend them if you wanted one char at a time.

If you swap in `itertools.izip()` for zip you can deal with very large data too.

 

 

