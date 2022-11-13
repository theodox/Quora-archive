# What is the pythonic way to remove duplicate dictionary values and merge their keys? {'A': {'b': 7, 'c': 7}} should become {'A': {('b', 'c'): 7}}.

	author: Steve Theodore
	written: 2020-01-01
	views: 465
	upvotes: 15
	quora url: /What-is-the-pythonic-way-to-remove-duplicate-dictionary-values-and-merge-their-keys-A-b-7-c-7-should-become-A-b-c-7/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


There’s only ever going to be a single entry for a given key, so in the example of making

    {'A': {'b': 7, 'c': 7}} 

into

    {'A': {('b', 'c'): 7}

You can leverage the dictionary behavior in reverse. A function like this will take a dictionary and return a new dictionary whose keys are tuples of all the keys referencing the original value. It uses a [collections.defaultdict](https://docs.python.org/3.8/library/collections.html#collections.defaultdict) to quickly generate the reversed dictionary, and then a dictionary comprehension to re-reverse the dictionary into the tuple-key form:

    import collections
    
    def collapse_dict(original_dict):
     reversed = collections.defaultdict(list)
     for k, v in original_dict.items():
     reversed[v].append(k)
     return {tuple(vv): kk for kk, vv in reversed.items()}
    
    
    print(collapse_dict({'b': 7, 'c': 7}))
    
    # {('b', 'c'): 7}

To apply this to a nested dictionary like in the example:

    example = {'A': {'b': 7, 'c': 7}, 'B': {'c':1} } 
    reprocessed = { k: collapse_dict(v) for k, v in example.items()}
    print (reprocessed)
    # {'A': {('b', 'c'): 7}, 'B': {('c',): 1}}
