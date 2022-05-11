# Python Function versus Class: what is the difference between using either methods?

	author: Steve Theodore
	written: 2017-09-25
	views: 10314
	upvotes: 7
	quora url: /Python-Function-versus-Class-what-is-the-difference-between-using-either-methods/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


In classic [object oriented programming](https://code.tutsplus.com/articles/python-from-scratch-object-oriented-programming--net-21476), a class is supposed to bundle up some data along with specialty methods for manipulating that data. You might have a class representing an car which knows the position and direction of the car. You could uses the class’s functions (“[instance methods](http://metapython.blogspot.com/2010/11/python-instance-methods-how-are-they.html)”, to be more precise) to ‘drive’ the car, since steering involves changing both the position and orientation of the car in ways that can be pretty complex. Part of the value of using classes in this kind of situation is that you can hide the details of how the car actually works: if a front-wheel drive and a rear-wheel drive car handle differently you can make sub-classes to handle the difference transparently. Other parts of the program would not have to know which kind of car was involved, they’d just ask the car to drive and get the results. The essential thing about a class, though, is that it has its own data storage: after you ‘drive’ the car it’s position will change, but that copy of the car will still know where it its.

Classes are great for some kinds of problems, but they have a potential drawback: It’s hard to know what really happens when you call a method on a copy of a class. The whole idea is to hide some data inside the class instance —which works great when you’re trying to hide things but sometimes it means you’re not aware of everything that actually happens when you do it. The changes that happen when you call a function are known as “[side effects](https://en.wikipedia.org/wiki/Side_effect_(computer_science))” and they can cause a lot of bugs if not well understood. For example, your car class might have a method called ‘reset’ which returns the car to a particular position and orientation. If you call the reset function as a way of setting the car back to a know position but you don’t realize that the function also changes the orientation (or vice-versa) you can easily end up with bugs.

This leads some people to try and avoid classes while only using functions: a style known as [functional programming](https://www.ibm.com/developerworks/library/l-prog/index.html). Functions, as distinct from classes, dsn’t know anything about context: you could write a function that did the math to move and rotate a car, but if it were just a function and not part of a class you’d be responsible for passing in the initial position and orientation. You’d also have to take the result of the function and do something with it. a plain old function in this sense is like a mathematical function: you give it some inputs and it gives you an output, what you do with them is up to you. Keeping your functions and data completely separate has one important property: like mathematical functions but unlike classes, plain functions can be chained together to create more complex functions. This makes it easy to build up complex behaviors out of simple (and easily testable) building blocks.

In the real world, most programs are a mix of object-oriented and functional techniques. They’re both valuable and complementary to each other. Since most schools teach object-oriented programming it’s often easier to find bad examples, but both styles are valuable.



That said, this video should be required watching for anybody getting used to classes in Python — it makes the valuable point that simple, clear programs are always better than sticking to a programming concept.



