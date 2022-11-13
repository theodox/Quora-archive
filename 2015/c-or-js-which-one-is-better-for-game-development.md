# C# or JS, which one is better for game development?

	author: Steve Theodore
	written: 2015-10-11
	views: 3416
	upvotes: 6
	quora url: /C-or-JS-which-one-is-better-for-game-development/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Essentially Javascript is a good choice for relatively un-demanding browser games, but not much else.

Generally console and big-ticket PC games are dominated by C++: speed and very precise control over what happens right down on the hardware win out when you're trying to squeeze every ounce of performance out of a game.

JS has actually gotten pretty fast in recent years, but in the end it's not running that close to the metal. Moreover much of what makes JS cool - whether it's the flexibility of dynamic types or widespread support for asynchronous methods - also makes it hard to manage and debug in large, complex environments. So, it's great for making games that aren't very large or demanding (most of what used to be done in Flash, for example, can be done in JS these days). 

C# sort of splits the difference: it's less performant than C++ but it offers a more structured development environment and a more traditional, type-safe programming style then JS while still targeting a pretty broad array of machines. As the language of choice for Unity games it's also probably the easiest route for beginners, since many of the hardest problems in development (3d graphics, input hardware management, and AI navigation) are available as off-the-shelf components in Unity.

