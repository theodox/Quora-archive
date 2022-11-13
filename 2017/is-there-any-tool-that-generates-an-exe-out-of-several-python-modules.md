# Is there any tool that generates an .exe out of several Python modules?

	author: Steve Theodore
	written: 2017-12-11
	views: 349
	upvotes: 2
	quora url: /Is-there-any-tool-that-generates-an-exe-out-of-several-Python-modules/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


The first answer to [this StackOverflow question](https://stackoverflow.com/questions/14165398/a-good-python-to-exe-compiler) has a good roundup of most of the existing solutions.

You can also use IronPython to generate a .net binary for use on any CLR system, though IronPython does not have 100% parity with regular C python in terms of third party modules, or Jython to generate executable .jar files; again, Jython will not be compatible with CPython binary extensions.

Lastly there are transpilation solutions like [Nuitka](http://nuitka.net/pages/overview.html), which convert the Python code to C++ (or C, if you use [Cython](http://masnun.rocks/2016/10/01/creating-an-executable-file-using-cython/)) and then compiles that to a conventional exe. These solutions are faster than vanilla Python most of the time — but (like IronPython and Jython) they are limited to pure python code, rather than binary extensions — and the output exes aren’t python anymore. Some Python programming tactics won’t make sense in that kind of environment.

