# What can't I do with Python?

	author: Steve Theodore
	written: 2017-07-07
	views: 17904
	upvotes: 31
	quora url: /What-cant-I-do-with-Python/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


As a practical matter, anything that involves high-speed computation or massive memory access is going to be more performant if done in native code (note that’s _not_  just C++ — you can get native code from lots of languages from D to Rust to god-help-you Fortran). Well written Python is actually pretty fast for a lot of tasks, but it’s not as fast as equally well written native code because there’s no indirection through the Python virtual machine. The extra work that happens in that layer means not only less speed but also, on mobile platforms, more battery drain.

Another thing that’s Python isn’t really meant for is front end web development. While you can actually write browser code in Python (using [Skulpt](http://www.skulpt.org/) or [Brython](https://www.brython.info/)) it’s going to be slower than the equivalent Javascript because it has to be emulated in Javascript. For this kind of thing I like [Transcrypt, ](http://www.transcrypt.org/)which “compiles” Python source into pretty decent Javascript code; it’s a nice compromise between speedy performance and Python’s cleanliness and developer-friendly paradigm.

And that’s the real point. The choice between languages does not have to be entirely binary. You _can_  do anything in C++ — it’ll just be painfully slow to develop. Or you _can_  do the same things in Python; they’ll just be painfully slow at runtime. Or you can isolate the performance sensitive parts of your work into native code and glue them together with Python, giving you freedom to choose between development speed and runtime speed with more granularity. Other points on that spectrum of tradeoffs include things like [Cython, ](http://cython.org/)which lets you write Python but compile it to native code modules that are as fast as C. Most Pyhon gui applications use a native GUI toolkit — something like QT — controlled by Python logic.

Purists on either end of the spectrum might not like it but in the end a lot of real-world jobs are best done with a mix of technologies and not just the ones that different programmers feel most comfortable with.

