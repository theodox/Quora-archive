# Why should Python be used for teaching an 'Introduction to Programming' course for a first year undergrad computer science class, instead of C/C++/Java?

	author: Steve Theodore
	written: 2015-01-21
	views: 778
	upvotes: 1
	quora url: /Why-should-Python-be-used-for-teaching-an-Introduction-to-Programming-course-for-a-first-year-undergrad-computer-science-class-instead-of-C-C++-Java/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


It really depends on the class. "Computer Science" can focus on algorithms, code organization and programming paradigms, or it can focus on how bits are moved around inside the computer. 

Python is an excellent choice for an introduction to the abstract topics, since it is less prone to errors that have nothing to do with algorithm design (such as slipped pointers) and has lower syntactic overhead, while still offering access to advanced conceptual features like meta-programming and functional programming. 

Python goes out of it's way to hide the other side - the 'what's really going on under the hood' side - of computing. If the course intends to highlight that side, then python is a poor choice. Many common CS jobs like 'implement a linked list' or 'sort this array' aren't worth bothering with in Python -- you can do them for the hell of it, but as far as Python is concerned they're basically artifacts of other languages. If you think those kinds of jobs are important for the course, then again Python is not a good choice.

If the design of the course involves application development, it's much more likely you can get students to create functional applications (albeit, slower ones!) using Python thanks to the large, well documented and always-available standard library. There's a [fun thread on StackExchange](http://codegolf.stackexchange.com/questions/44278/debunking-stroustrups-debunking-of-the-myth-c-is-for-large-complicated-pro) comparing 'simple' programs in C++ and many other languages which gives a good flavor of what the obstacles to light weight app development can be. Again, the weight you place on this depends on the aim of the course.

If the course is designed around performance sensitive questions - showing how to optimize not merely the algorithms but their concrete implementations, C/C++ give much more precise control over all aspects of the process. 

If you're considering Java, you should also consider C# which is very similar but offers a few more paradigms. The existence of a good standard IDE with fast autocompletion makes a difference to beginners too :)

