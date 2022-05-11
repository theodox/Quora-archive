# How do you tolerate programming in C++ after tasting the sweet fruit of C# or Python?

	author: Steve Theodore
	written: 2017-01-31
	views: 1222
	upvotes: 14
	quora url: /How-do-you-tolerate-programming-in-C++-after-tasting-the-sweet-fruit-of-C-or-Python/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


__Grudgingly__ . I actually have to discipline myself to focus on the work at hand rather than simply complaining all the time.

The balance between the problem-solving domain and the language-knowledge domain in C++ is terrible, particularly if your work is on the ‘solve this problem right now’ end of the spectrum rather than the ‘solve this problem super efficiently for a long time to come’ end of same.

To some degree, of course, this is just grumbling — it’s subjectively very unpleasant to work in a language you’re not good at when you _know_  you could do it better in another environment. To some degree it’s bad match of tool and task: most of what I do doesn’t benefit from C++’s real strengths (performance, precise control over memory and object lifecycle) but it does suffer from the it’s drawbacks (syntactic clutter, easy ways to commit suicide, and the archaic header / include system). If your job is optimizing a rendering engine, you care a lot about precise management of allocations and highly optimized math.

If your job — like mine — is a series of microtasks like “find all of these things where the artists have set two values out of whack and fix or delete them as appropriate” you just want to strangle the system which makes you wait 10 minutes to see if your two-line change is valid, which makes you dig around to know the precise way in which the data you’re trying to modify was stored in memory, or blows up like the Hindenburg because you forgot an asterisk in a logging macro.

OTOH, try writing something like a fast N-dimensional convex hull generator in pure Python (_without_ Numpy — that’s cheating!). It will make you appreciate, however resentfully, what C++ brings to the table.

