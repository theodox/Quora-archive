# What is good and clean event-driven programming in Python? I am currently experiencing what's called "Callback Hell" and want to know how to do it right.

	author: Steve Theodore
	written: 2016-05-10
	views: 22043
	upvotes: 24
	quora url: /What-is-good-and-clean-event-driven-programming-in-Python-I-am-currently-experiencing-whats-called-Callback-Hell-and-want-to-know-how-to-do-it-right/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Based on the comments above, here's a general strategy. Obviously the details matter a lot, of course.

Basically you'll have two parts. 

 The __event object__ or the '__publisher'__ is responsible for maintaining a list of all the functions which should be called when an event happens. It has a fire() method which loops over that list and calls all of the functions in turn. It probably also should have methods for managing the list (removing a function from the list it's no longeer needed). 

The __handlers__ or '__subscribers'__ are functions that you're going to call when the event actually happens. The only tricky bit there is that you need to control the signature of the handlers so the event can call them without doing any extra introspection.

Here's an ultra minimal example:


    class Event(object):
    	def __init__(self, *args):
    		self.handlers = set()
    		self.args = args
    
    	def add(self, fn):
    		self.handlers.add(fn)
    
    	def remove(self, fn):
    		self.handlers.remove(fn)
    
    	def __call__(self, *args):
    		'''fire the event -- uses __call__ so we can just invoke the object directly...'''
    		runtime_args = self.args + args
    		for each_handler in self.handlers:
    			each_handler(*runtime_args)
    
    class ExampleObject(object):
    	'''publish start and stop events'''
    	def __init__(self):
    		self.start = Event('started')
    		self.stop = Event('stopped')
    
    def example_handler(*args):
    	''' reacts to an event'''
    	print "example handler fired", args
    
    
    fred = ExampleObject()
    fred.start.add(example_handler)
    fred.stop.add(example_handler)
    
    fred.start()
    fred.stop('optional extra arg')

That should produce 


    example handler fired ('started',)
    example handler fired ('stopped', 'optional extra arg')

The main management issues are:


__Exception handling.__ you need to decide if the handler has to be exception safe or not. If not the above code is more or less OK, but if you don't want a bad subscriber to bring down the whole program you need to decide how to cope with an exception and whether or not to 'un-subscribe' the offending handler.

__Memory management.__ The example only uses a function as a handler; unless you del() the function you don't have to manage it's lifetime. However you'll often want to have either callable objects or member functions as handlers/subscribers . If so, you probably need to use weak references rather than the naive set used in the example -- otherwise the event handlers will end up keeping objects alive after they ought to have dropped out of scope and should be garbage collected.

__Metadata:__ The example includes a little bit of metadata -- the string that gets passed in as the Event()s are declared. Your application might need more or less than this. More metadata usually means more coupling, which is not ideal. However if your handlers all have the (*args, **kwargs) signature you can always pass the data and then decide at the handler level if you care about it or not.

Good reference: [The Observer Pattern in Python](https://newcircle.com/s/post/1743/2015/06/17/tutorial-the-observer-pattern-in-python)


Example of the basic idea in action: [theodox/mGui](https://github.com/theodox/mGui/blob/master/mGui/events.py)


