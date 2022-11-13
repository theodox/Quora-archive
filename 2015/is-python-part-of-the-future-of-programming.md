# Is Python part of the future of programming?

	author: Steve Theodore
	written: 2015-02-14
	views: 1771
	upvotes: 3
	quora url: /Is-Python-part-of-the-future-of-programming/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Python (4 slots down from top right) on [this survey of language popularity](http://redmonk.com/sogrady/2015/01/14/language-rankings-1-15/) isn't going away soon. It's too useful. 



![](https://qph.fs.quoracdn.net/main-qimg-31b15bae1fc0a59f2176287ece7d85b1)


Despite what the static typing zealots would have you believe, there are many different ways to achieve software stability. Type checking accounts for some kinds of problems up front, but also creates vastly more code to handle the same problems (3 to 10 times more, depending on who you listen to) More code -- especially the kind of 'more code' you get in a lot of statically typed languages where you're basically cutting and pasting and changing type declarations -- is an invitation to slight differences in behavior between similar-but-not-identical implementations, and a permanent tax on future refactors. The effect of static typing on bugs is dwarfed by the difference between [managed and unmanaged memory](http://macbeth.cs.ucdavis.edu/lang_study.pdf), but I don't see C or C++ going anywhere soon.

If all a good language required was good habits, we'd only be writing Haskell. But other things, like programmer productivity, good standard libraries, readability and flexibility all matter too.

