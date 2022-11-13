# How do you create a palindrome checker with Python's loop and if statements (python, loops, palindrome, development)?

	author: Steve Theodore
	written: 2020-05-31
	views: 498
	upvotes: 4
	quora url: /How-do-you-create-a-palindrome-checker-with-Pythons-loop-and-if-statements-python-loops-palindrome-development/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


    def is_palindrome(word):
    	for a, b in zip(word, reversed(word)):
    		if a != b:
    			return False
    	return True	

This is not the most efficient possible version (among other things, it could quit after the halfway point). However it’s a good compromise between terseness and readability, and it showcases why Python style doesn’t need to lean on tradition C-style for blocks.

Of course if you don’t really care about implementation and just want the palindrome check, the loop is superfluous:

    def is_palindrome(word):
     return word == reversed(word)

If you want to super clear you could use `word.lower()` in place of `word` in these examples to make them case insensitive.

