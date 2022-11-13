# In Python can we add a dictionary inside a dictionary? If yes how can we access the inner dictionary using the key in the primary dictionary?

	author: Steve Theodore
	written: 2015-01-23
	views: 62940
	upvotes: 14
	quora url: /In-Python-can-we-add-a-dictionary-inside-a-dictionary-If-yes-how-can-we-access-the-inner-dictionary-using-the-key-in-the-primary-dictionary/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Your example works if you quote the key values and change the variable name: don't use dict(), it's a reserved word.




    my_dict={
    'a':{'b':10,'c':20},
    'd':{'b':30,'c':40}
    }
    
    print my_dict['a']['b']
    # 10
