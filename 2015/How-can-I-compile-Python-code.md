# How can I compile Python code?

	author: Steve Theodore
	written: 2015-01-25
	views: 1644
	upvotes: 4
	quora url: /How-can-I-compile-Python-code/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Python 'compiles' when it runs: If you have a python file, pass it to a python intepreter and it will run, compiling itself to bytecode as a side-effect of being run. The usual syntax is 

python my_file.py

running the python intepreter without any arguments, or with the -i flag, puts you into interactive mode where you can type python directly and execute it as you go.

The python interpreter command flags and arguments are documented [ here](https://docs.python.org/2/using/cmdline.html)

