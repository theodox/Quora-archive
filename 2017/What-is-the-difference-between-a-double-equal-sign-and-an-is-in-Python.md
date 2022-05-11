# What is the difference between a double equal sign(==) and an 'is' in Python?

	author: Steve Theodore
	written: 2017-04-25
	views: 4885
	upvotes: 7
	quora url: /What-is-the-difference-between-a-double-equal-sign-and-an-is-in-Python/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


`=` is an assignment: it puts the value on the right into the variable on the left.

`==` is an equality test, it’s asking if the left hand expression means the same thing as the right hand. Equality is a concept that you can control — for example [a class can define “equality” any way it wants by overriding the `__eq__` metho](http://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes)d for itself.

There’s a separate identity check, the keyword `is` which returns true if the left hand variable and the right hand variable point at the same object memory.

