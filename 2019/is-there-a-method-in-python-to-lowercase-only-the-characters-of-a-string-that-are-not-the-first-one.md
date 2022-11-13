# Is there a method in Python to lowercase only the characters of a string that are not the first one?

	author: Steve Theodore
	written: 2019-02-15
	views: 184
	upvotes: 3
	quora url: /Is-there-a-method-in-Python-to-lowercase-only-the-characters-of-a-string-that-are-not-the-first-one/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


For a string that’s just a single word, there’s `.title()`:

    “ABCD”.title()

produces `Abcd`

If you aren’t sure its a single-word string, then

    my_string = “ABC DEF GHI”
    my_string[0].upper() + my_string[1:].lower()

produces `Abc def ghi`

Note that both of these are forcing the first letter to uppercase — if you don’t want that then it’s

    my_string[0] + my_string[1:].lower()
