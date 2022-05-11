# I'm a beginner at programming. Why must we use a unit test in our project?

	author: Steve Theodore
	written: 2015-02-02
	views: 391
	upvotes: 4
	quora url: /Im-a-beginner-at-programming-Why-must-we-use-a-unit-test-in-our-project/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Here's the story I always tell unit test newbies:

I once had a set of tools for checking files in and out of [Perforce](http://www.perforce.com/). It used another library which was did simple file path manipulations and formatting: consistent slashes, etc. All pretty simple. I tweaked the behavior of the file path class to change the way it did equality testing so that path names would match regardless of case, since windows is not case sensitive. That all worked fine -- it was even tested. But... the next day all the unit tests for the perforce server started failing. The tests in the first module, which checked things in and out of perforce, failed because the perforce server was running on a linux box - the server thought that a/b/c and A/B/C were different files, and so tests for expected content went haywire - it turned out we had hundreds of files which existed in multiple casing! 

The moral of the story is there is no such thing as an innocent change in behavior. Even a really trivial change in one place can reveal a bad assumption in another. Without tests, the edit trail is extremely muddy: programmer A says "this worked until today! I didn't do anything! not my fault!" while B says "I'm just working on file paths, it can't be my fault!" Tests guard the interfaces between systems in ways that human beings rarely can.

