# What should guide a programmer regarding when to use a function or an object in python?

	author: Steve Theodore
	written: 2015-02-25
	views: 259
	upvotes: 3
	quora url: /What-should-guide-a-programmer-regarding-when-to-use-a-function-or-an-object-in-python/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


The general rule of thumb is pretty simple: an object has _state_ , that is, it needs memory of some internal settings or variables. A function is stateless: it might contain temporary variables but these are not going to outlast a given run. 

It's common for people to confuse 'objects' and 'data structures'. The classic object examples in how-to books are always things like :



    class Person (object):
     def __init___ (first, last, age):
     self.firstname = first
     self.lastname = last
     self.age = age



However, by itself this is really just a data structure: you could do it with a dictionary or a [namedtuple](https://docs.python.org/2/library/collections.html#collections.namedtuple). 

The key difference between a real object and a dumb data structure is self-awareness. If you wanted the object to 'remember' things about operations it could perform, it would be a good candidate for an object:



    class Person (object):
     def __init___ (first, last, age):
     self.firstname = first
     self.lastname = last
     self.age = age
    
     def get_older(self):
     self.age += 1
    
     def change_name(self, newname):
     self.lastname = newname
     
     def introduce(self):
     print "Hi! My name is %s %s" % (self.firstname, self.lastname)


Done this way, other bits of code can make a person get older or change their name without knowing the details of how that happens (if you were using a dictionary, on the other hand, you'd need to know that 'age' is a number, that it goes up by 1 every year, and so on). Objects are great for exposing functionality and hiding details. 

A lot of coders like to use objects to group related functions together even though the functions have no shared state. You can spot this when the object's functions never check the _self_  parameter: if you're not using _self_  in any way, you probably don't want to be an object. As you can see in these examples, though, Person needs to know about itself -- Python helpfully reminds us by passing _self_  into the functions -- to do its job. 

On the other hand when you don't actually need the self -- like when you just want to group related functions into a common namespace -- it's easy to use a python module for that. You still get the organizing benefits of nested names but you don't have any state to manage.

