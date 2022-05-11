# What is an algorithm for generating all possible combinations of a given set of letters (e.g. 'a', 'b', 'c', 'd', 'e')?

	author: Steve Theodore
	written: 2015-07-19
	views: 17619
	upvotes: 6
	quora url: /What-is-an-algorithm-for-generating-all-possible-combinations-of-a-given-set-of-letters-e-g-a-b-c-d-e/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


If you're not interested in the algorithm for its own sake, but just need the results, the standard libraryy [itertools](https://docs.python.org/2/library/itertools.html) module does this for any iterable collection:



    import itertools
    itertools.permutations('abc')
    [i for i in itertools.permutations('abc')]
    [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]



For a practical example of using recombination to generate variants (in this case for a spell checker) you can check out [spelchek](https://github.com/theodox/spelchek), which does transpositions and deletions inside of words to identify possible spelling corrections.

