# What does '^' mean in python?

	author: Steve Theodore
	written: 2016-05-21
	views: 714
	upvotes: 6
	quora url: /What-does-mean-in-python-2/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


It’s the [Exclusive or](https://en.wikipedia.org/wiki/Exclusive_or) “XOR” operator. It’s mostly used for bit operations:

    1 ^ 1 = 0
    1 ^ 0 = 1
    0 ^ 1 = 1
    0 ^ 0 = 0

It works on bits, so when used with numbers other than 1 and zero it’s flipping powers of 2:

    6 ^ 1 = 110 ^ 001 = 111 = 7
    6 ^ 2 = 110 ^ 010 = 100 = 4
