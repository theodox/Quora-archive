# Is it possible to create a game engine with one language and then create game logic with another? I.e, create the engine with C++, then create the AI/missions with something else, like Python?

	author: Steve Theodore
	written: 2017-09-26
	views: 408
	upvotes: 4
	quora url: /Is-it-possible-to-create-a-game-engine-with-one-language-and-then-create-game-logic-with-another-I-e-create-the-engine-with-C++-then-create-the-AI-missions-with-something-else-like-Python/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Yes, this is very common.

Most coders I know tend to prefer Lua as a scripting language because it’s leaner and less prone to garbage collection hitches than Python, but if you’re a good python programmer — and if you’re disciplined about moving computationally challenging pieces into compiled code — a scripting language can be a huge boost to developer productivity.

Almost any language can be used as a scripting language — Naughty Dog, for example, uses a home-grown variety of Lisp. Python is a middle-of-the-pack choice: it’s a good flexible language, its clarity and generality make it good for complex systems, but it’s not particularly fast or memory efficient. A lot really depends on the game — if you’re in a tight performance environment something lean, like Lua, might be a better choice; for a slower moving game with complex mechanics Python is probably more appropriate.

