# Can I run a Python script in Windows without Python installed?

	author: Steve Theodore
	written: 2017-08-09
	views: 83028
	upvotes: 20
	quora url: /Can-I-run-a-Python-script-in-Windows-without-Python-installed/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Well, you can’t run it without _any_ Python of any kind — without some kind of Python your script is just a text file with a funny extension.

You can however get a non-install (ie, non-registry) version of Python — for example, one that runs off of a thumb drive. The go-to for that used to be Portable Python, which is not actively supported any more but is available [here ](http://portablepython.com/wiki/Download/)for Python 2.7.6.

There are number of web-based Python out there. [PythonAnywhere](https://www.pythonanywhere.com/) offers free accounts; [PyPy.js](http://pypyjs.org/) is free but has no local storage; and [Brython interactive mode](https://www.brython.info/tests/console.html?lang=en) offers a pretty complete python console emulated in Javascript. All of these share one critical limitation: they’re not running on your local machine, so they can’t access your local filesystem.

In a similar vein, if the script doesn’t need to actually touch the disk drive, you can install the [Chrome Python](https://chrome.google.com/webstore/detail/python/nodpmmidbgeganfponihbgmfcoiibffi?hl=en) extenstion which runs Python in your browser. Unfortunately it lives inside the browser’s security sandbox so it can’t touch your system directly which makes it pretty limited.

More here:
[3 and 1/2 ways to try Python without installing it](http://pythonforengineers.com/3-and-12-ways-to-try-python-without-installing-it/)

