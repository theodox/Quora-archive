# If I disassemble a Python bytecode, can I run it on any hardware, even without an interpreter? If not, how can I read the assembly instructions that Python bytecode gives to my x86 processor?

	author: Steve Theodore
	written: 2017-10-15
	views: 397
	upvotes: 1
	quora url: /If-I-disassemble-a-Python-bytecode-can-I-run-it-on-any-hardware-even-without-an-interpreter-If-not-how-can-I-read-the-assembly-instructions-that-Python-bytecode-gives-to-my-x86-processor/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Python byte code only runs on the [Python virtual machine](https://leanpub.com/insidethepythonvirtualmachine/read)— it's not native code on any platform . The actual instructions that hit the hardware come from your interpreter — which could be one of several competing implementations (pypy for example will produce a different series of machine instructions than Cpython, IronPython will go through MSIL, and so on).

There are projects which try to use Python bytecode — the pre-interpreted version that is spit out by [py_compile](https://docs.python.org/2/library/py_compile.html) — to do special tasks. For example [Batavia](https://pybee.org/project/projects/bridges/batavia/) converts bytecode to Javascript for web applications and [VOC](https://pybee.org/project/projects/bridges/voc/) does the same for the JVM.

Allison Kaptur’s talks on the Python VM are great background on what’s really going on.





If you really wanted x86 you could try a static transpilation of your project using something like [Nuitka](http://nuitka.net/). Of course at that point it will be a compiled C++ program but you’ll be able to disassemble it and get the x86.

