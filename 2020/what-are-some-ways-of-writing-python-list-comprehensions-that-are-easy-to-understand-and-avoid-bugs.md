# What are some ways of writing Python list comprehensions that are easy to understand and avoid bugs?

	author: Steve Theodore
	written: 2020-06-23
	views: 293
	upvotes: 5
	quora url: /What-are-some-ways-of-writing-Python-list-comprehensions-that-are-easy-to-understand-and-avoid-bugs/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Honestly, the best indicator of list-comp maintainability is line length. If your editor starts complaining about the number of characters in your comprehension, you’re probably making an unreadable and thus hard-to-maintain monster.

For example you might need to reformat phone numbers from a list of human-entered phone numbers. You’d like to normalize these (removing parentheses, dots, and dashes, etc) then filter out any without area codes, then output them into neatly formatted list.

For readability, here’s the pieces:

    def as_digits(numstring):
     return "".join(j for j in numstring if j.isnumeric())
    
    def is_10_digits(numstring):
     return len(numstring) == 10
    
    def phone_format(numstring):
     return f"({numstring[:3]}) {numstring[3:6]}-{numstring[6:]}"

Even with these helper methods doing the actual work its still easy to make a monster list comp by trying to jam this all together in one place. Any individual piece is easy, but doing the sequence of operations in a single expressions produces this icky beast:

    # DONT DO IT LIKE THIS:
    
    result = [phone_format(j) for j in [x for x in [as_digits(f) for f in phone_nums] if is_10_digits(x)]]

This is wrong on so many levels, but above all its (a) unreadable and (b) has to create two different lists in memory before assembling the final list.

On the other hand if you pull it apart into pieces, it becomes way less ugly and easier to maintain:

    normalized = [as_digits(f) for f in phone_nums]
    only_valid = [n for n in normalized if is_10_digits(n)]
    result = [phone_format(v) for v in only_valid]

However there’s a free way to make this better. The first two operations are still creating complete lists in memory, which is wasteful — especially if you have a lot of data. But once you’ve got it working you can convert them from list comprehensions to generator comprehensions with a simple punctuation change:

    normalized = (as_digits(f) for f in phone_nums)
    only_valid = (n for n in normalized if is_10_digits(n))
    result = [phone_format(v) for v in only_valid]

Now the first two steps will be processed stepwise, and don’t become independent lists in memory; it’s leaner and faster and more readable than the original monster. You could technically nest them using parens in the big original example — but it would just be an invitation to trouble and a huge hit to readability.

