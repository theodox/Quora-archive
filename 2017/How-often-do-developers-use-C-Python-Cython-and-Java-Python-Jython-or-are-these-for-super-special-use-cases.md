# How often do developers use C-Python (Cython) and Java-Python (Jython), or are these for super special-use cases?

	author: Steve Theodore
	written: 2017-05-17
	views: 2548
	upvotes: 3
	quora url: /How-often-do-developers-use-C-Python-Cython-and-Java-Python-Jython-or-are-these-for-super-special-use-cases/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


There’s really two very different things here.

Jython (and IronPython, the Python that runs on the CLR) are not primarily about speed differences or about precompilation — they’re about being able to use Python in a different ecosystem. With Jython you can write python code that works with Java APIs; with IronPython you can write Python that works with Dotnet objects.

It’s very common that you’ll get be stuck working with software that only has a public API for Java or Dotnet. For example Microsoft’s Team Foundation Server only used to expose a public API in Java. I was able to write a bug server in Jython that used the Java API without having to actually write the whole application in Java. In a more extreme case, I’ve[ hacked a Python interpreter into the Unity game engine using IronPython](https://theodox.github.io/2013/python_in_unity) in a couple of hours, where including a “real” CPython would have been much more involved.

Cython, on the other hand, is a very different beast. CPython is the vanilla Python intepreter, the one that runs when you type `python` from your command prompt. Cython is a C-code generator that takes Python files (with some special markup if you really care about speed) and transpiles them into C. It’s a great way to make C extension modules for speeding up important parts of your program, but it’s not really intended for compiling complete programs — which isn’t to say that lots of people don’t try to use it that way. If you really want to go that route there are other compilers like [Nuitka](http://nuitka.net/) and [shedskin](https://github.com/shedskin/shedskin) that are intended for whole-app compilation.

Unfortunately all of the solutions for compiling Python run up against Python’s big weakness — it’s hard to manage all the dependencies (which might be pure python or might be C extensions), and which might or might not be easily compatible with your compiled program. The more modules your program depends on the higher the likelihood of something going sideways. Python’s openness tends to work against nice easy ‘buttoned up’ compilation schemes.

