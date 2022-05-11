# Python desktop development vs native windows app in WPF?

	author: Steve Theodore
	written: 2014-11-08
	views: 21
	upvotes: 0
	quora url: /Python-desktop-development-vs-native-windows-app-in-WPF/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


You can split the difference by using IronPython with either WinForms or WPF. 

[IronPython.net /](http://ironpython.net/)

The Python app will be slower than C# but on modern machines there are not that many jobs where performance is bound by CPU - usually its network or IO that slows you down these days, unless you're writing a game or doing 3d rendering or something similarly math-heavy. IronPython can compile an app to .exe, although that only matters for passing out files, not performance.

You can also host IronPython inside a C# app and leave the UI work in straight C# while doing the logic in Python.

You could get C# like perfromance using Boo, which looks a lot like Python but is typed and compiled more like C#:

[BOO - Home](http://boo.codehaus.org/)

