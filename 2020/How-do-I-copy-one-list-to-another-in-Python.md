# How do I copy one list to another in Python?

	author: Steve Theodore
	written: 2020-02-16
	views: 455
	upvotes: 3
	quora url: /How-do-I-copy-one-list-to-another-in-Python/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


If you really want a duplicate (and not just another reference to the original) the usual shorthand is

    list_b = list_a[:]

The notation [:] is a [slice notation](https://stackoverflow.com/questions/509211/understanding-slice-notation); it means “all the elements in list b”. You could use the same notation to take all the elements of the first list except for the first one like this:

    list_b = list_a[1:]

or only the 3rd, 4th and 5th elements like this

    list_b = list_a[2:5]

There’s also a module called copy which will make an independent copy; ie

    import copy
    list_b = copy.copy(list_a)

however it’s wordier and offers no extra advantages here.

