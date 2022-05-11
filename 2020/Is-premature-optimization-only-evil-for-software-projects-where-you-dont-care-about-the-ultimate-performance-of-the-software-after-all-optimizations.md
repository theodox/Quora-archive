# Is premature optimization only "evil" for software projects where you don't care about the ultimate performance of the software after all optimizations?

	author: Steve Theodore
	written: 2020-06-11
	views: 181
	upvotes: 3
	quora url: /Is-premature-optimization-only-evil-for-software-projects-where-you-dont-care-about-the-ultimate-performance-of-the-software-after-all-optimizations/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


No — if it’s really premature, it’s just a mistake.

Optimization takes time and effort (and money) — spending two weeks squeezing an extra millisecond of out the routine you’re working on today means you have two less weeks next month when you stumble into a badly designed algorithm where you’d pick up whole seconds after optimizing.

Optimizations need to be based on a good understanding of how a system fits together and where it’s bottlenecks really are. You also need to understand the final runtime environment: optimizing for speed frequently leads to memoization or caching: great for speed but not so nice on an embedded device with 16k of RAM. Optimizing for IO speed might lead you to store data in ways that are bad for runtime cache hits.

There are a million ways to “optimize.” You’ll only have time to do a few optimizations so you should try to ensure they are the right ones. Obviously you want your first pass to be designed in ways that won’t make it impossible to optimize later: If you know you’re likely to be CPU bound you’ll try not to pick a CPU-intensive, memory-light solution as your first pass. But actually optimizing — which real profiling data, not just rules of thumb and hunches — should be approached in the proper context.

