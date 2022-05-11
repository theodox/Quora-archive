# How do I replace strings with numbers in Python?

	author: Steve Theodore
	written: 2020-02-21
	views: 1906
	upvotes: 2
	quora url: /How-do-I-replace-strings-with-numbers-in-Python/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


The safest way — which doesn’t require you to know what kind of number (an integer, a float, or perhaps a long integer) you’ve got — is to use the __ast__ module, which has a nice method for evaluating the meaning of a piece of text without the risks of blindly evaluating a string which might be _“import os; os.rmdir(‘c:/’)”_ 

So, the basic trick is just:

    import ast
    my_number = ast.literal_eval("35")

_literal_eval()_ does what the python interpreter does with a string and will give you what the string looks like. If your string would not be a valid expression when typed into the python console the function will raise a _ValueError._ If you supply a string which is a valid something else — for example, “[]” which would give you a literal list not a number — _literal_eval()_  will happily return that. So, you’ll want to validate your result, something like this:

    import ast, numbers
    
    def number_from_string(mystring):
    	value = ast.literal_eval(mystring)
    	if isinstance(value, numbers.Number):
    		return value
    	else:
    		raise ValueError ("'{}' is not a number".format(my_string)

Since _literal_eval()_ will raise a _ValueError_ on bad strings, you can trust that this method will give you a valid number or raise a _ValueError_ on both bad strings and non-numeric strings.

