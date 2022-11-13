# What is Python mainly used for in the real world today? Is it beneficial to use Python for desktop apps?

	author: Steve Theodore
	written: 2015-01-26
	views: 188600
	upvotes: 65
	quora url: /What-is-Python-mainly-used-for-in-the-real-world-today-Is-it-beneficial-to-use-Python-for-desktop-apps/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Python excels at integration tasks. Many applications use Python as an embedded scripting language; while it's not as light as Lua, it's much more versatile and has all sorts of ready-made tools so it makes a great tool for gluing things together. For example, [3D sofrware like Maya](http://www.autodesk.com/products/maya/overview) includes Python which can be used for automating small user tasks, or for doing more complex integration like talking to databases and asset management systems.

Python is also very popular in web development, though primarily on the 'back end' side. The combination of easy extensibility, good iteration time, and good integration with database and other web standards makes it a popular choice. Quora, for example, has a [lot of Python code](https://www.quora.com/Why-did-Quora-choose-Python-for-its-development-What-technological-challenges-did-the-founders-face-before-they-decided-to-go-with-Python-rather-than-PHP).

The two places where Python hasn't made big inroads are high-performance applications -- Python is definitely slower than C or C++ for compute-heavy tasks -- and desktop applications. Python expects a 'live' python environment - it's possible, but not simple, to pack up a python application into a single executable file. This makes it hard to distribute python to non-technical users.

