# Under which circumstances will "__name__" have some other value than "__main__" in Python?

	author: Steve Theodore
	written: 2018-04-04
	views: 474
	upvotes: 4
	quora url: /Under-which-circumstances-will-name__-have-some-other-value-than-main__-in-Python/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


__name__ will be the name of the module if the file is being imported rather than executed. Often the if name == __main__ block is used in code that can do double duty as an importable module and as executable code. The if-check allows you to isolate code that only wants to run in as a script from code that is part of module initialization.

