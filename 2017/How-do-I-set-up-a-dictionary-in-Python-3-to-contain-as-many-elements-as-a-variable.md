# How do I set up a dictionary in Python 3 to contain as many elements as a variable?

	author: Steve Theodore
	written: 2017-03-04
	views: 428
	upvotes: 1
	quora url: /How-do-I-set-up-a-dictionary-in-Python-3-to-contain-as-many-elements-as-a-variable/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


If you’re just interested in prefilling the dict, the easy way is

    { n + 1: np.array([0,1]) for n in range(how_many_you_need) }

However if you know the arragement is going to be that static and predictable you don’t need a dictionary — you just need a list:

[ np.array([0,1]) for n in range(how_many_you_need) ]

You won’t get much out of using dictionary if the keys really are going to be sequential integers — a list is fine for that.

You can also get out of the need for prefilling the list using a [defaultdict](https://docs.python.org/2/library/collections.html#collections.defaultdict), which will create a new entry for you if you hit an empty key.

    from collections import defaultdict
    
    def new_entry():
     return np.array([0,1])
    
    example = defaultdict(new_entry)
    print example[1]
    # np.array([0,1])

In some contexts this makes for cleaner coding — but if you need to know that a key is actually present in the dictionary — instead of just asking and getting value back — defaultdict will confuse you more often than not.

