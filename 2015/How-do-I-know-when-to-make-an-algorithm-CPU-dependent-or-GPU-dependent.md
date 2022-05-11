# How do I know when to make an algorithm CPU dependent or GPU dependent?

	author: Steve Theodore
	written: 2015-11-09
	views: 448
	upvotes: 1
	quora url: /How-do-I-know-when-to-make-an-algorithm-CPU-dependent-or-GPU-dependent/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Good answers from both [Salman Ul Haq](https://www.quora.com/profile/Salman-Ul-Haq) and [Jeff Kesselman](https://www.quora.com/profile/Jeff-Kesselman) . The only thing I'd add is that for most coders and most general-purpose situations old-fashioned CPU programming is simply easier to write and debug. That's changing slowly as tools get better and knowledge of the crazy stuff you need to do to really leverage GPUs spread more widely.

That and the fact that in most game projects, anyway, we simply alternate between being CPU and GPU bound at high frequency -- basically as soon as something seems not to be the bottleneck people pile onto it and start abusing it till it becomes the obvious pain point :) _If it's not overloaded, you're not trying hard enough_ seems to be the unofficial game dev motto.

