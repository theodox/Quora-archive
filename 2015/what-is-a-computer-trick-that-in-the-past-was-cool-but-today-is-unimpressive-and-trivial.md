# What is a computer "trick" that in the past was cool, but today is unimpressive and trivial?

	author: Steve Theodore
	written: 2015-06-07
	views: 4757
	upvotes: 29
	quora url: /What-is-a-computer-trick-that-in-the-past-was-cool-but-today-is-unimpressive-and-trivial/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


When I started in graphics in the early 90's, this SGI Crimson was the premiere graphics workstation in the world (seen here in Jurassic Park)

![](https://qph.fs.quoracdn.net/main-qimg-f1bf022db328b1baefbfb6c0228112ff-c)

We had a few of these in a loft office in Chicago. They threw off enough heat to let us leave the heat off in Chicago winters.

They are slighly less powerful than my iPhone.

And almost all of the things that been rendered irrelevant come from that fact: we're so many generations down the road from the formative eras of the late 80's and early 90's that many, many optimizations that made sense when processors were 60-100X slower and RAM was incredibly costly (generic DRAM back then started around $30 per megabyte, and SGI's markup drove that _way_  higher: in inflation adjusted terms I'd guess just a bit less than $100/mb on those machines. Today DRAM runs $0.0056 per mb: 17 _thousand times cheaper)._ 

So: computing lore is full of vestigial optimizations which make a lot of sense in a slow, RAM-poor world that are not important in realistic applications. The difference between a Python application that takes up 10mb on disk and executes in 50 milliseconds and a C++ one that its 128kb and takes 1 millisecond is rarely going to be perceptible to anybody except the authors of the two programs. However -- depending on the context -- the real-world time that the authors spend on their respective programs can easily vary by 2-5 times as well. If you're writing a game, the extra hit makes sense; if you're writing a file inventory tool it's just silly to spend all that human time to save milliseconds and bytes nobody will ever see.

