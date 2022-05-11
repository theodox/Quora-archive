# What is an explanation in detail of what happens in these decorations in Python?

	author: Steve Theodore
	written: 2015-01-29
	views: 366
	upvotes: 2
	quora url: /What-is-an-explanation-in-detail-of-what-happens-in-these-decorations-in-Python/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Decorators replace the decorated function with a new function that takes the original function as an argument -- the idea being that you can add a 'wrapper' around the original function that is reusable among many functions.

In this case, the double-decorator looks like an attempt at creating a decorator that can take an argument . The more usual idiom for this is to create a decorator _class_ instead of a function, and to capture the arguments in the class init, but this example works like this:

1) the `tags` function grabs the argument ("p") into the variable `tag_name`
2) It defines a function called tags_decorator, which inherits the value of tag_name via a closure (see the answer to [Closures in Python](http://stackoverflow.com/questions/4020419/closures-in-python) for more detail)
3) `tags_decorator` is a 'wrapper function' - it generates a new function but taking the argument `func` and putting a little extra behavior around it. You'll note that `tags` returns the function itself, and not the result of the function. Wrappers basically replace references to the functions they wrap with references to themselves.
4) the tricky bit -- `tags_decorator` itself contains another wrapper function, which does the same trick: insert itself in place of the function it wraps (you could abuse this ability in lots of ways : you could completely ignore the function that is being wrapped if you really wanted to! Not a good idea, but possible)
5) The end result is that the decorator applies, effectively, another decorator. 
As I said, this is a dodge to allow the decorator to take an argument - ordinary decorator functions expect the decorated function as an argument, so they don't allow arguments of their own.

