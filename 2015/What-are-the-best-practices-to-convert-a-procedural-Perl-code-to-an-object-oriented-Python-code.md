# What are the best practices to convert a procedural Perl code to an object-oriented Python code?

	author: Steve Theodore
	written: 2015-06-15
	views: 503
	upvotes: 3
	quora url: /What-are-the-best-practices-to-convert-a-procedural-Perl-code-to-an-object-oriented-Python-code/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


This is a great opportunity to think about the way you want the actual code to work, independent of the way it works right now. You have experience with domain so you can design an API that makes sense for the problem, and you have working example code so you can probably steal lots of hyper-local things (like the right regex for formatting a piece of data or the correct steps for creating a new account). 

A scratch re-write using the perl version as reference will be cheaper and more reliable over the long run -- and probably even the lower-mid-term as well.

