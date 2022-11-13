# If C is so strong a programming language why can't it replace Python in AI and data science?

	author: Steve Theodore
	written: 2019-03-26
	views: 2497
	upvotes: 28
	quora url: /If-C-is-so-strong-a-programming-language-why-cant-it-replace-Python-in-AI-and-data-science/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


The most popular Python data science packages actually are C, under the hood : Numpy and SciPy, for example, are mostly in C for speed because they deal with relatively straightforward problems on data which is very homogeneous and well suited for a strongly typed language. So C already _is_ very popular in data science, just hiding in the background doing what it’s best at.

That said, you could theoretically do AI with any language from Visual Basic to COBOL. That wouldn’t make all of those languages equally popular, however, with developers who wanted to get any work done. Execution time and memory costs are two of the important factors that go into a coding ecosystem, but they aren’t the only ones: developer convenience, accumulated knowledge, and the availability of good libraries and standards matter a lot, too.

Python’s popularity in Data Science stems from two distinct sources.

First off is a good collection of libraries which make both the core job (data processing) and the necessary side work (collecting and formatting data before it’s analyzed) fairly easy. A huge fraction of the work in an AI / ML project is getting the data collected and marshaled into an appropriate format, and Python — with great libraries for interfacing with a lot of sources and strong, well maintained libraries for the analysis as well — offers a lot of ready-made solutions to the problems which have to be solved _before_  you get to work on your awesome new data project, like scraping data out of public websites or collating data from a bunch of similar-but-slightly-different databases.

Second, Python easy to experiment with. It’s not as fast or as “safe” as a compiled systems language. However it’s quicker for developers — allowing you to try a bunch of experimental approaches cheaply. Python excels at the quick-and-dirty, “experimental science” side of AI — but once the hypotheses are worked out, though, it’s often a good idea to convert over to a systems language for speed and reliability.

