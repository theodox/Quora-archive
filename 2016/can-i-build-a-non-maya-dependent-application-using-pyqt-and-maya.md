# Can I build a non-Maya dependent application using PyQt and Maya?

	author: Steve Theodore
	written: 2016-10-13
	views: 470
	upvotes: 1
	quora url: /Can-I-build-a-non-Maya-dependent-application-using-PyQt-and-Maya/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


You can make an pyqt or pyside app with Python and without maya.

You can also add more UI to maya using Python and QT.

If you really wanted to you could make an app using the mayapy interpreter and qt just like you could fit any other Python interpreter but it would be a bad idea — it would be very hard to distribute and would have no advantage over a vanilla Python/QT app if you did not need maya functionality.

There is nothing magical about how maya works with QT- if you get QT and a wrapper like pyside or pyqt you don't need maya.

