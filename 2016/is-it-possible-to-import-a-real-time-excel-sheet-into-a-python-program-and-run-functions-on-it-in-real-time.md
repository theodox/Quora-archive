# Is it possible to import a real-time excel sheet into a Python program and run functions on it in real-time?

	author: Steve Theodore
	written: 2016-05-10
	views: 2105
	upvotes: 1
	quora url: /Is-it-possible-to-import-a-real-time-excel-sheet-into-a-Python-program-and-run-functions-on-it-in-real-time/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


The easy way out -- removing the realtime constraint -- would be to use the builit-in [CSV module](https://docs.python.org/2/library/csv.html), which has no external depenencies and is very straightforward. 

For realtime control you can use [PythonWin32](https://sourceforge.net/projects/pywin32/) and control a running instance of Excel via COM. As [this stackOverflow question demonstrates](http://stackoverflow.com/questions/441758/driving-excel-from-python-in-windows) it's possible but kind of ugly... bccause COM. 

If you want the excel user to initiate actions you'll need to install an event handler in your python code. [Here's an example of a Python server reacting to excel events](https://github.com/SublimeText/Pywin32/blob/master/lib/x32/win32com/demos/excelRTDServer.py). This is much more complex than just reading and writing CSVs -- it requires each half of the relationship to know how the other works and its also asynchronous.

