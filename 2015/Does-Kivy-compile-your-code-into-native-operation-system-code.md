# Does Kivy compile your code into native operation system code?

	author: Steve Theodore
	written: 2015-01-19
	views: 1752
	upvotes: 0
	quora url: /Does-Kivy-compile-your-code-into-native-operation-system-code/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


You can run a kivy application directly from .py files, although you can use [pyinstaller](https://github.com/pyinstaller/pyinstaller/wiki) to create standalone 'applications' that bundle the python files and kivy together. 

It's not a highly secure method, since it's not difficult to unpack the pyinstaller packages and see the original files. Python is [not easy to obfuscate](http://stackoverflow.com/questions/3344115/obfuscating-python-code), although you can discourage casual snooping by compiling to .pyo files (details in that last link). 

This link [How do I protect Python code?](http://stackoverflow.com/questions/261638/how-do-i-protect-python-code) contains some more discussion of how to hide python code if you really want to. But it's not trivial.

