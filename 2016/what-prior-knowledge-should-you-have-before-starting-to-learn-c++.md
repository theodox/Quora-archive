# What prior knowledge should you have before starting to learn C++?

	author: Steve Theodore
	written: 2016-05-08
	views: 865
	upvotes: 5
	quora url: /What-prior-knowledge-should-you-have-before-starting-to-learn-C++/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


If you're already a coder, you can probably just dive right in.

 All imperative languages are all fairly similar. C++ is a bit more gotcha-ridden than most; it's got a long and convoluted history, supports many different sub-genres of programming, and allows you very direct access to the underlying hardware, so it's a pretty rocky _first_  language . Still, if you're past the point of being surprised by brackets, semicolons, and so on you'll be able to manage it. [Accelerated C++](http://amzn.to/1rIsVKR) is a popular starting point because, unlike a lot of hard-core C++ books it doesn't try to walk you through implementing every data structure and algorithm from scratch: it does what most real people do and uses libraries for common tasks. [A Tour of C++ ](http://amzn.to/1rBZk67) is a good book if you've got non-C++ experience and want to pick up the language itself as a language: it highlights the core features rather than teaching programming. If you've a bit of experience with C-style memory management, [Effective Modern C++ ](http://amzn.to/1rIrFY8) is a good rundown of how it's supposed to be done now.

One thing you will need to be aware of is the archaeology of C++. In computer terms it's a pretty old language and has gone through several distinct eras with different best practices and paradigms. C++ programmers who have lived through them all don't always know how to orient people who haven't. [Scott Meyers ](https://www.youtube.com/results?search_query=scott+meyers) is a pretty good guide to disentangling all of those strata in the language though I don't know of any single book that's the one go-to.

Personally, I would not recommend C++ as a first language. Because it has such a long history it's got a lot of slightly mysterious rules that trip up even experienced programmers. Detailed control over memory allocations, access, and usage are great for advanced users, but is a distraction from the more basic job of becoming familiar with basic coding techniques. C++ has evolved through several distinct periods and the lessons of one aren't always applicable in later iterations -- this adds a lot of burden if you're trying to teach yourself because you need to version check all of the advice you're getting. There are a number of languages which share the same basic syntax and structure but aren't quite so punishing for first timers, C# being the most obvious candidate.

