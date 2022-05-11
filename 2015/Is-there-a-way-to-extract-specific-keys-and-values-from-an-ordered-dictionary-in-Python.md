# Is there a way to extract specific keys and values from an ordered dictionary in Python?

	author: Steve Theodore
	written: 2015-06-24
	views: 150327
	upvotes: 31
	quora url: /Is-there-a-way-to-extract-specific-keys-and-values-from-an-ordered-dictionary-in-Python/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


OrderedDictionaries are just dictionaries with some additional properties. So, you can use the usual dictionary methods to get at their contents: 

__square-brackets__ if you know the key:


    variable = dictionary[key]


__.get()__ if you're not sure the key is there:


    variable = dictionary.get('key', None)


__.keys()__  to iterate over the keys:


    for key in dictionary.keys():
     print "dictionary includes", key


__.items()__  to get all of the key-value pairs:


    for key, value in dictionary.items():
     print key, "=", value



iterating over the dictionary directly also the same as .keys(), however (just like with regular dictionaries) you have to remember not to change the dictionary's keys during a loop:



    for key in dictionary:
     print "dict has", key
    
    # DON'T DO THIS!
    for key in dictionary:
     dictionary[key + "_extra"] = key
