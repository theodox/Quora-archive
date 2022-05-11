# How (or where) can I test my Python code?

	author: Steve Theodore
	written: 2015-05-25
	views: 9328
	upvotes: 2
	quora url: /How-or-where-can-I-test-my-Python-code/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Python is usually run in an intepreter - a program (itself usually with significant parts in C) that reads you code and runs it. The minimal case is:

1) Write a text file , for example the classic 'hello world" script. Save it with the .py extension
2) start the interpeter and point it at your file: ie, "python.exe helloworld.py" (on OSX or Linus you probably just type 'python') 

That runs the program. Any errors will be reported if the program does not run correctly.

The interpreter can also run in 'interactive mode'. Instead of passing in a file, you can just run "python.exe" and you'll get a prompt like a DOS or Terminal prompt. You can try out Python statements one line at a time. This is handy for getting used to the basics or trying out an idea fast.

You can also try things out online using something like [repl.it](https://repl.it/languages/Python3), [Online Python Interpreter](http://mathcs.holycross.edu/~kwalsh/python/) or [Skulpt](http://www.skulpt.org/), all of which run the interpreter in your browser. You won't be able to use some functions or libraries in the online versions but they are helpful for messing around.

Python is free and can be downloaded for most OS's ([Michael Johnson-Moore](https://www.quora.com/profile/Michael-Johnson-Moore) has the link)

