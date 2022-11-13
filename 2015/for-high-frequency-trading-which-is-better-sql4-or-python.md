# For high frequency trading, which is better, SQL4 or PYTHON?

	author: Steve Theodore
	written: 2015-05-25
	views: 735
	upvotes: 3
	quora url: /For-high-frequency-trading-which-is-better-SQL4-or-PYTHON/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


If you're talking 'milliseconds matter", vanilla python is not a great choice although important components of a system might still be do-able in Python (there a good example, and some cautionary tales, in [High Performance Python](http://shop.oreilly.com/product/0636920028963.do) by Micha Gorelick and Ian Ozwald). 

SQL will probably be a component of any system that deals with a lot of data: writing a database system with high performance and reliability is already a huge job, it would be high risk to reinvent that. However SQL by itself is only going to store and retrieve data: the actual business logic and communications with trading servers will have to done in some other language.

