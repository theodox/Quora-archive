# Does “@classmethod” simply indicate that the method is inheritable by all subclasses?

	author: Steve Theodore
	written: 2017-10-09
	views: 350
	upvotes: 4
	quora url: /Does-“-classmethod”-simply-indicate-that-the-method-is-inheritable-by-all-subclasses/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


No, it means that the method doesn’t get a reference to `self` (ie, to an individual instance of the class) but it does get one to the class definition.

    class ClassMethodVInstanceMethod(object):
    
     CLASS_VAR = 99
    
     def __init__(self, val):
     self.instance_var = val
    
    
     def instance_method(self):
     	# self is the instance that called the method, but it can also
     	# see the class variables
    
     print "my value is ", self.instance_var, "and the class value is ", self.CLASS_VAR
    
    
     @classmethod
     def class_method(cls):
     	# `cls` is ClassMethodVInstanceMethod the definition
     	# not any particular instance. Can't see instance variables 	
    
     	print "i don't have instance vars, but my class var is ", cls.CLASS_VAR
    
    # you need an instance for this:
    
    inst = ClassMethodVInstanceMethod(999)
    inst.instance_method()
    
    # but not for this:
    
    ClassMethodVInstanceMethod.class_method()
