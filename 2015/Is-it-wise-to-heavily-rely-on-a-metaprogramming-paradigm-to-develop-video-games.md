# Is it wise to heavily rely on a metaprogramming paradigm to develop video games?

	author: Steve Theodore
	written: 2015-02-01
	views: 238
	upvotes: 1
	quora url: /Is-it-wise-to-heavily-rely-on-a-metaprogramming-paradigm-to-develop-video-games/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


With great power comes great responsibility. For a small team where the architect of the meta-programming system is not going to leave (or get run over by a bus) it can be a huge productivity booster. 

For a big team it's going to take a lot of code ownership away from junior coders because they will be dependent on behind-the-scenes magic. If they don't get deeply indoctrinated in the way the system works it will become unmaintainable if the original guru departs for any reason; if they do have to learn it, that's a lot of time taken away from front line tasks. It probably only makes sense in a context where the game domain is so specific and so badly adapted to other paradigms that you can't think of any other way to do it. In most other cases, simple (and more debuggable!) is better.

