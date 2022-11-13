# How do I make a table from a dictionary and manipulate the values in Python?

	author: Steve Theodore
	written: 2014-12-01
	views: 466
	upvotes: 0
	quora url: /How-do-I-make-a-table-from-a-dictionary-and-manipulate-the-values-in-Python/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Here's a good resource for python string formatting:
[Python String Format Cookbook](https://mkaz.com/2012/10/10/python-string-format/)

To get 2 decimal places for a value you'll use the format() function and a specification string like :

 "{:.2f}".format(your_number_here)
 # this is calling 'format' which is a function offered by every string

To line up your values, you can use the .center, .ljust, and .rjust functions:

 "1234".center(10) 
 # produces " 1234 "

 "1234".ljust(10)
 # produces " 1234"

 "1234".rjust(10)
 # produces "1234 "

To format a whole class at once, the map() function us great for applying another function to every item in a list. Thus:

 def align(val):
 return "{:.2f}".format(val).center(10)
 values = map (align, d['dog'] )

Use .join() to string together a whole set of values (like the results of the last line above)

 values = map (align, d['dog'] )
 dataline = "dog".ljust(10) + "|".join(values)

