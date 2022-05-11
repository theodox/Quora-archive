# Is Kivy a viable alternative to native development while still achieving professional results? If yes, what are the drawbacks and trade-offs?

	author: Steve Theodore
	written: 2015-02-01
	views: 644
	upvotes: 1
	quora url: /Is-Kivy-a-viable-alternative-to-native-development-while-still-achieving-professional-results-If-yes-what-are-the-drawbacks-and-trade-offs/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Kivy is pretty, and the API is fairly pythonic. It's also NUI (touch) capable. The main problem is distribution: the packaging process uses a variety of different routs for different target platforms so you will have to invest in some sort of build system if you are targeting more than one OS. And, like all python app development, managing your dependencies and zipping them up into a distribution is not trivial.

