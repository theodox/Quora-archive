# Is there a way to convert Python code into JavaScript?

	author: Steve Theodore
	written: 2015-09-14
	views: 12395
	upvotes: 6
	quora url: /Is-there-a-way-to-convert-Python-code-into-JavaScript/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


There are a few other alternatives to PyJS as well:

[Transcrypt ](https://github.com/QQuick/Transcrypt)is a PS to JS transpiler for python 3.6. It’s produces pretty high-quality JS but does not try to port lots of the python standard library. The JS output can be mapped to python source using source maps, which is a big help to debugging. Since it’s JS at runtime, it interoperates well with other JS libraries. [Here’s ](https://theodox.github.io/extra/pysteroids)an example of an asteroids game written in Transcrypt with Three.JS (note: does not work very well in MS Edge)

[PyPy.js: ](https://www.rfk.id.au/blog/entry/pypy-js-first-steps/)uses Emscripten and PyPy to compile python to JS: [rfk/pypyjs](https://github.com/rfk/pypyjs)

[RapydScript](http://rapydscript.pyjeon.com/) transpiles into human-readable JavaScript (like CoffeeScript, below) . It's not a 100% port of Python, however, but it does cover most of the core language. The same author had a previous project called [PyvaScript](https://www.allbuttonspressed.com/blog/django/2010/07/PyvaScript-Pythonic-syntax-for-your-browser) which is much more limited and JavaScript-y but does clear up some syntax issues

[jaredly/PJs](https://github.com/jaredly/PJs)

[p2k/PyCow](https://github.com/p2k/PyCow)

Here's a roundup from a few years ago (2011): [A survey of Python to Javascript converters](http://chargen.blogspot.com/2011/08/survey-of-python-to-javascript.html). And one from the author of RapydScript: [Pyjamas Alternatives for Web Developmen](http://blog.pyjeon.com/2012/09/17/301/)t.

If -- like me -- you just hate curly brackets there's [CoffeeScript](http://coffeescript.org/), which is a Javascript dialect: structurally it's JavaScript but syntactically it's mostly Python (with a little bit of Ruby thrown in). It's pretty slick and (unlike most alternatives) fairly widespread. However, for perspective, here's a[ look at some of the warts](http://www.walkercoderanger.com/blog/2014/03/coffeescript-isnt-the-answer/).

[Brython](http://www.brython.info/) and [Skulpt](http://www.skulpt.org/) are both Python interpreters written in JavaScript (that is however not what you asked for). You can write scripts in Python and they'll be interpreted in the browser. Because the interpreter runs in JS it's pretty slow but it's adequate for a lot of tasks where network time or resource loads dominate computation costs. If you don't mind SilverLight, [IronPython](http://ironpython.net/) has a Silverlight based interpreter that runs on the DotNet DLR -- so it's much faster than a JS based interpreter.

