# What are some methods in Python Dictionary?

	author: Steve Theodore
	written: 2014-12-28
	views: 664
	upvotes: 3
	quora url: /What-are-some-methods-in-Python-Dictionary/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


The methods are listed in the [docs](https://docs.python.org/2/library/stdtypes.html?highlight=dict#dict). However the most important ones are:

__keys()__ 
__ Gives you all the keys in the dictionary _at the time when you called keys()._  You can loop over a dictionary with a simple _in_  loop:



    for item in this_dictionary:
     print this_dictionary[item]



but if you try to change the dictionary during the loop, you'll get an error:



    for item in this_dictionary:
     if item.startswith("x"):
     del(item)



will not work because you're changing the container while looping over it. However since keys() makes a copy before looping you can do this:



    for item in this_dictionary.keys():
     if item.startswith("x"):
     del(item)



__items()__ 
Items(), like keys() makes a copy of the dictionary contents, but it returns the dictionary as a key-value pair. This makes it easy to get both the key and the value in a loop. The common method is:



    for key, value in this_dictionary.items():
     print key, "\t", value



which uses Python multiple assignment to get the key and value out of items() in one line.

__get()__ 
Get allows you to specify a default value for a key that is not present when you try to retrieve it. If you have a dictionary like this:



    my_dict = { "a": 1, "b': 2}



You'll get an error if you try to get a key that is not there:



    c_value = my_dict["c"]



Will raise a KeyError. However you can do this to get a fallback value when "c" is not present in the dictionary:



    c_value = my_dict.get("c", 0)



If "c" is in the dictionary you'll get it's value, but if "c" is missing you'll get a zero value instead of a KeyError.

