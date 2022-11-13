# How can I implement the biconditional logical operation in Python?

	author: Steve Theodore
	written: 2020-02-15
	views: 903
	upvotes: 11
	quora url: /How-can-I-implement-the-biconditional-logical-operation-in-Python/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


If you mean the logical AND (what in other languages is written as & or sometimes &&) it’s just the keyword and:

    if n < 50 and n > 25:
    	print ("valid")

If you mean the special python syntax for chained comparisons, you get that implicitly by chaining operators:

    if 25 < n < 50:
    	print ("valid")

The above two snippets are identical. Obviously the latter one only works for values that support greater than / less than comparisons, the first one works for any kind of comparison:

    if day == "Friday" and hour > 4:
    	goof_off()

Python numbers also offer bitwise logical operators like those you see in C-style languages. So, for example, you can use familiar logical operators (&, |, ~ for negation and ^ for XOR) but they’ll be operating on the underlying binary values of the the numbers. So, it’s valid to write something like

    if a & b:
    	print ("both")

but it’s a bad idea to use this as a mental shorthand for the keyword and. That snippet means “if the logical AND of numbers a and b has any bits set” whereas the more standard

    if a and b:
    	print ("both")

means “variables a and b are both ‘truthy’”, a concept which extends to things like non-empty strings or lists, or custom classes that report their own status as boolean.

