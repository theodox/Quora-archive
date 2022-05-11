# Can I use input() without assigning a variable in Python? If yes, how can I use it?

	author: Steve Theodore
	written: 2019-08-31
	views: 147
	upvotes: 3
	quora url: /Can-I-use-input-without-assigning-a-variable-in-Python-If-yes-how-can-I-use-it/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


You can use it inline, if you really want to:

    print(input())

It’s probably bad practice because you can’t really be sure what you’re going to get and processing some arbitrary set of characters inline like this is unlikely to make for readable code. Probably the only legitimate case is

    input(“press enter to continue”)
