# In Python, does time.sleep() work for float or just integers, and if only for integers how can I get the program to pause for 1.87 seconds?

	author: Steve Theodore
	written: 2019-03-11
	views: 791
	upvotes: 10
	quora url: /In-Python-does-time-sleep-work-for-float-or-just-integers-and-if-only-for-integers-how-can-I-get-the-program-to-pause-for-1-87-seconds/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


time.sleep() is in floating point seconds — but it makes no specific guarantees about the actual resolution of the time, so you can’t make hard assumptions that 1.87 will pause for exactly 1.87 and not, say, 1.87003 or something like that. The best you could hope for would be “about 10–15 milliseconds” of precision. Between the underlying OS and the precision of floating point numbers ( in general, you’ll have to expect a little slop.

More detail on precision [here.](https://stackoverflow.com/questions/1133857/how-accurate-is-pythons-time-sleep)

