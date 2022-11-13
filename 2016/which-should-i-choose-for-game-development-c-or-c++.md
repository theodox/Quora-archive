# Which should I choose for game development: C# or C++?

	author: Steve Theodore
	written: 2016-01-20
	views: 5862
	upvotes: 6
	quora url: /Which-should-I-choose-for-game-development-C-or-C++/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Generally C++ is the hardcore game-developer favorite: it allows you to get closer to the 'real' behavior of the hardware and to directly control your allocation of resources -- particularly of memory, which is all-important in performance intensive games. 

C# is not terribly slow compared to C++ but it is slower. More importantly, since C# manages your memory for you there will be situations in which the C# runtime decides to garbage collect and clean up memory without asking permission. This almost always causes a notable lag -- it can sometimes be measured in seconds where game programmers are used to counting in milliseconds. It's possible to avoid this will careful attention to memory usage -- or by doing an end run around C#'s memory management -- but at that point you've lost one of the prime bonuses of C# development, which is not having to worry about messing up your memory allocations.

In games where memory pressure is not too tight (games with less content) or where there are variations in pace which can hide occasional garbage collections C# is a fine environment: lots of Unity games use C#. However for really sensitive, high-performance applications C++ is going to have a higher top-end throughput, albeit at the cost of a more complex development process.

