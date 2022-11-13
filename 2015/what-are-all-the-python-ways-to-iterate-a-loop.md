# What are all the Python ways to iterate a loop?

	author: Steve Theodore
	written: 2015-01-30
	views: 1281
	upvotes: 2
	quora url: /What-are-all-the-Python-ways-to-iterate-a-loop/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


for fancy stuff there's also the [ itertools](https://docs.python.org/2/library/itertools.html) module. It's great for managing iterators in concert. In ordinary Py you'd do something like 


    for x in range (10):
     for y in range (10):
     print x,y 


To print out all the combinations of 0 - 9 from (0,0) to (9,9). That's not too bad, but you add more inner loops it gets nasty. With itertools you can split out the iteration part from the organization:


    import itertools
    for item in itertools.product(range(10), range(10)):
     print item


The difference isn't big here but it's a huge help if you're trying to manage more dimensions, or if the loop generation functions are more complex than calling range.

Itertools also allows you to do things like synchronise multiple iterators:


    import itertools
    for item in itertools.izip_longest ('abcde', [1,2,3,4,5,6]): 
     print item


which will produce


    ('a', 1)
    ('b', 2)
    ('c', 3)
    ('d', 4)
    ('e', 5)
    (None, 6)



There's a ton of fun stuff to play with in the module -- too much to detail here. Check it out! Also [itertools - Iterator functions for efficient looping](http://pymotw.com/2/itertools/) is a good intro, as is [A gentle introduction to itertools](http://jmduke.com/posts/a-gentle-introduction-to-itertools/).

