# Is there a newer, more modern and faster alternative to Python? Is it worth learning it for web development only?

	author: Steve Theodore
	written: 2017-05-01
	views: 2754
	upvotes: 6
	quora url: /Is-there-a-newer-more-modern-and-faster-alternative-to-Python-Is-it-worth-learning-it-for-web-development-only/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


A lot depends on whether you mean front-end or back-end web development.

If you are thinking about browser side code you really ought to learn JS — and I say that as someone who finds JS distasteful.

There are cool and interesting ways to get around JS — alternate syntaxes like [CoffeeScript](http://coffeescript.org/) and [Rapydscript](http://www.rapydscript.com/), and efforts to create a more traditional structured web toolkit like [TypeScript](https://www.typescriptlang.org/). There also transpilers which “compile” other languages into JS; my favorite right now is [Transcrypt](http://www.transcrypt.org/) (which turns Python into JS) but you can find [plenty of other tools for converting some other language to Javascript](https://github.com/jashkenas/coffeescript/wiki/list-of-languages-that-compile-to-js) too.

All of these tools and approaches share two things:
1. they reflect the fact that a lot of people don’t like JS and will go to great lengths to get out of working with it.
2. They all depend on JS.

So even if you plan on working _around_  JS for now it’s important to be pretty familiar with it for the foreseeable future; even if it drives you nuts you’ll almost certainly be working with JS libraries and tools that expect JS style content. It’s the cost of doing business in the front end. Maybe things will change when [WebAssembly](http://webassembly.org/) becomes ubiquitous and the tools catch up… but that’s a ways off.

If you’re looking at the back end — the code that runs on the server side rather than in the browser — you have a lot more options. There are plenty of great stacks out there in a variety of languages, you should probably look for one that reflects your strengths as a developer today while you learn web dev. Once you’ve got some experience you’ll be in a better position to evaluate the relative merits of different stacks. Python tools like [Django](https://www.djangoproject.com/) are a great way to get started with web dev and to learn its many ups and downs fast.

If you’re really looking for a ‘more modern’ back end alternative, my subjective feeling is that [Swift](https://swift.org/blog/) does the best job of capturing Python’s agility and expressiveness in a fast, type-safe environment… but that’s going to be a personal thing for a lot of people. There are also languages like [Nim ](https://nim-lang.org/)and [boo](https://github.com/boo-lang/boo) which borrow a lot of Python’s spirit and syntax, although both of these are fairly niche right now.

