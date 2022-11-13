# Is it possible to have static class variables or methods in Python?

	author: Steve Theodore
	written: 2019-03-22
	views: 396
	upvotes: 3
	quora url: /Is-it-possible-to-have-static-class-variables-or-methods-in-Python/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Yes, though it’s often indicative of “thinking in other languages” when done in Python.

If you just want to have access to a method without the need to create a class, just make a method in a Python module. You get the global accessibility and the neatness of namespacing without the extra overhead of creating a do-nothing class to host the method. A lot of recent Python converts create classes just to host static methods, but that’s an anti-pattern in Python — it’s just a habit of thought left over from more traditional OO paradigm.

    # in file MyUtilityModule.py
    
    def no_need_for_static():
     return "hello world"
    
    # In another file:
    
    import MyUtilityModule
    MyUtilityModule.no_need_for_static()

If you do have a class which needs static helper functions, you can [use the `](https://stackabuse.com/pythons-classmethod-and-staticmethod-explained/)@staticmethod[` or `](https://stackabuse.com/pythons-classmethod-and-staticmethod-explained/)@classmethod[` decorators](https://stackabuse.com/pythons-classmethod-and-staticmethod-explained/) to keep the no-instance-needed code together with the class that it has to know the details about. A good example would be a class that handles some kind of resource with complex setup requirements — you might want to use a `@classmethod` to create and return a properly configured instance using a more user-friendly api instead of having a monstrously complicated constructor.

The syntax is pretty simple (Python 3 here — the only difference in 2 is that your class has to inherit from `object`:

    class SomeUtiityClass:
     CLASS_VAR = 123
     # declared outside the constructor, this variable
     # is accessible to all instance of SomeUtilityClass
     # or as 'SomeUtilityClass.CLASS_VAR'
    
     def __init__(self, *args, **kwargs):
     # some complex initialization logic here based on the arguments
     @staticmethod
     def static_construct(number):
     # in this form the function has no default argument (no 'self' or 'cls'
     # you can of course have other arguments
     return SomeUtilityClass(number, context = SomeUtilityClass. CLASS_VAR)
     # note that the static version needs a hard coded class
     # reference here
    
    	@classmethod
     def class_contruct(cls, number):
     # this version gets 'cls' instead of self -- it's a 
     # reference to the class from which this was called
     # this is often useful for creating child classes which use different class variables to customize behaviors. 
     # unlike the static example above, there's no need to 
     # hardcode the class reference:
    
     return cls(number, context=cls.CLASS_VAR)
     # a derived class with a different CLASS_VAR
     # will automatically get the correct value
     # and return the correct derived type

The best use case for a classmethod in Python is for tracking shared state. Syntactically this:

    class Counter:
     VALUE = 0
    
     @classmethod
     def increment(cls):
     cla.VALUE += 1

Appeals to a lot of people over this:

    # module Counter.py
    
    VALUE = 0
    def increment():
     global VALUE
     VALUE += 1

However they are functionally about the same.

