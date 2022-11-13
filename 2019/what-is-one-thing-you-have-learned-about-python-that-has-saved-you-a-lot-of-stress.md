# What is one thing you have learned about Python that has saved you a lot of stress?

	author: Steve Theodore
	written: 2019-11-27
	views: 4872
	upvotes: 12
	quora url: /What-is-one-thing-you-have-learned-about-Python-that-has-saved-you-a-lot-of-stress/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


I’d say it was the catalytic influence of this video, by Python core developer Jack Diederich



The essential point is that a lot of Python OOP practice is just cargo-cult programming: imitation of the way things work in other languages, performed in a manner that confers no actual benefits.

There have been times in my Python career when I’ve felt like going with the flow of the language — using first-class functions, namedtuples and dictionaries rather than writing a ton of chatty little classes — was somehow not professional enough. I used to feel like just solving the problem didn’t count, if you didn’t introduce a bunch of elaborate abstractions. But — thanks to Jack, and several years worth of other out-and-produce procedural programming Pythonistas — I’m don’t sweat having a low-class style anymore. There are still times when you need the scaffolding of a class (usually, when you’re dealing with lots of things at once that all have to maintain independent state). However those times are a lot less common than you might think if you are still thinking in C# or Java or C++.

Giving up on classiness has helped me relax a lot, and generally to write code that is more concise with less conceptual overhead.

