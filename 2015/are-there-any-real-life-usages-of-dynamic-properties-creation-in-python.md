# Are there any real-life usages of dynamic properties creation in Python?

	author: Steve Theodore
	written: 2015-01-22
	views: 155
	upvotes: 1
	quora url: /Are-there-any-real-life-usages-of-dynamic-properties-creation-in-Python/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


It's a common approach to data which is not rigidly formed. For example, data coming out of a NoSql database may have very variable formats, but it's still useful to be able to wrap the data in objects that have common behaviors. Dynamic property addition can be a useful trick there.

It can also be a useful trick in marshalling objects for remoting frameworks: If you make a JSONRPC call into python, all you're passing in is an dictionary or dictionary-of-dictionaries. If the receiver wants to wrap that in an object, property addition is one strategy to deal with the variability of the source data without being too rigid about it's format.

It's not a super common python idiom because undefined problems are something programmers -- even loosey-goosey python programmers -- avoid when possible. But these issues do happen in real life and this is a decent method for coping when they do.

