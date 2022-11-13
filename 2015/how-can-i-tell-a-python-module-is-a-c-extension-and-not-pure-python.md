# How can I tell a Python module is a C extension and not pure Python?

	author: Steve Theodore
	written: 2015-05-27
	views: 276
	upvotes: 1
	quora url: /How-can-I-tell-a-Python-module-is-a-C-extension-and-not-pure-Python/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


You'll need to find the actual module files and check: if they have .so or .pyd extensions they are binaries; .py, pyo, and .pyc are all 'pure python'

