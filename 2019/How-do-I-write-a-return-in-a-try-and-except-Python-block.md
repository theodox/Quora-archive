# How do I write a return in a try and except Python block?

	author: Steve Theodore
	written: 2019-09-01
	views: 645
	upvotes: 8
	quora url: /How-do-I-write-a-return-in-a-try-and-except-Python-block/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


By itself try/except won’t interfere with a return. So this will always return 999 and never print:

    try: 
     return 999
    except:
     print("failed to return")

However this might not work:

    try:
    	return numerator / divisor
    except:
    	print ("failed to return")

If `divisor` is zero, the return value will be `None` which might not be what you want. In a case like that you can have a fallback return inside the except block:

    try:
    	return numerator / divisor
    except ZeroDivisionError:
    	return 0
