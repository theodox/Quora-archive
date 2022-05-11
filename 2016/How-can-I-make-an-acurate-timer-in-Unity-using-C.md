# How can I make an acurate timer in Unity using C#?

	author: Steve Theodore
	written: 2016-05-08
	views: 5365
	upvotes: 0
	quora url: /How-can-I-make-an-acurate-timer-in-Unity-using-C/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


A coroutine-based timer is going to be limited by the update frequency of the underlying game loop, which isn't guaranteed to be consistent. If you hit something that causes a particular frame to run long (most commonly a garbage collection, but it could be anything which ties up the CPU) your coroutine isn't going to keep ticking during the hitch. It will check again on your _next_ frame -but if that next frame happens 1.1 seconds after you started the timer... well, that's what you get.

