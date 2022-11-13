# Why use a for loop instead of a while loop if a while loop does everything they do and more? The while loop seems to be more versatile. Are there any benefits or is it purely conventional?

	author: Steve Theodore
	written: 2015-09-12
	views: 11068
	upvotes: 27
	quora url: /Why-use-a-for-loop-instead-of-a-while-loop-if-a-while-loop-does-everything-they-do-and-more-The-while-loop-seems-to-be-more-versatile-Are-there-any-benefits-or-is-it-purely-conventional/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


They are basically the same: in most languages _for_ is just a helpful piece of syntax wrapped around an invisible _while._ However that doesn't make them interchangeable: they really do different jobs. You can manhandle them into doing each other's jobs but only by ignoring code-flow and readability.

A for loop is intended to iterating over a range or collection. It's implicitly a traversal of a set, with defined beginning and end points. In ordinary usage it's going to end without explicit user intervention, although it's explicit breakouts or skips can be added with _break_ , _continue_  or similar instructions. From a logic and code-flow standpoint, a for loop is about __dealing with repetitive data__ . "Do this to every item in this list" or "Collect the data from every one of these records".

A while loop, on the other hand, is about __program state__ , not about the data. It's generally used for putting the program into a mode and keeping it their until some condition triggers a mode switch: lots of servers are written inside a single _while (exit_requested = false)_  block with the expectation that the bulk of the execution will be inside that loop until a guardian flag is set by something that happens inside the loop. "Do this until I tell you to stop".

You can force each construct to behave like the other, but it's bad style: a while statement implies modality, where a for-loop expresses iteration. If you were in a really, really performance-constrained application you can save a few instructions by not ratcheting an index variable in a _for_ and instead tracking a counter flag in a _while_ , but the gains are probably not worth the extra effort for the vast majority of situations.

Here's a tweaky StackOverflow discussion of the machine level differences between _for_ and _while :_ _[http://stackoverflow.com/questions/2950931/for-vs-while-in-c-programming](http://stackoverflow.com/questions/2950931/for-vs-while-in-c-programming)_ 

