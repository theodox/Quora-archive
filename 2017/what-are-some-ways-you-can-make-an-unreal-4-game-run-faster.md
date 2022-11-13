# What are some ways you can make an Unreal 4 game run faster?

	author: Steve Theodore
	written: 2017-11-16
	views: 1972
	upvotes: 2
	quora url: /What-are-some-ways-you-can-make-an-Unreal-4-game-run-faster/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


This is way too broad a question for a single easy answer. However there are few steps you should always consider:

__Profile__ . The most important thing you can do is learn how to use the builtin [Unreal Profiler](https://docs.unrealengine.com/latest/INT/Engine/Performance/Overview/index.html) tool . It’s not perfect but it is a good way to highlight serious problems fast. It’s particularly good for helping you spot when you are being slowed down by graphics and when you are being slowed down by CPU work.
The most important thing about learning how to profile is that it lets you fix the real problems — not just the problems you read about on the internet somewhere. It’s not always going to be what you think, so follow the data and not your instincts.

__Watch out for blueprint costs.__ Blueprint is great for getting things prototyped or for simple behaviors like “turn on the light when the player enters the room”. Complex logic and big gameplay systems are much more expensive in blueprint than the equivalent code in C++. Use blueprint for what it’s good at — fast prototyping and lightweight behavior — and not as a replacement for writing code. You blueprint can’t compete with C++ for performance.

__Fewer Actors.__ Anything that ticks — an actor or a component — has to be managed. Lots of ticking components and actors always equals slower performance. Design your systems around a smaller number of actors and components instead of designing for a ton of tiny little independent pieces. It’s a shame that Unreal and many online examples encourage you to do to the wrong thing. But it’s the wrong thing.

__Recycle__ . Spawning entities at runtime is expensive and slow, and it’s likely to cause memory garbage collection hitches. It’s much more efficient to create a pool of reusable objects, spawning them all at startup but hiding them away until you need them. For example instead of spawning a brand new rocket every time your rocket launcher shoots, you should pre-create a set of rockets when the game starts, setting them all to invisible and turning off their ticks. Then when a rocket is fired you simply grab the next available rocket from your pool, set the position and other properties and turn it on. When it’s expended, turn it back off. This is way more performant and makes the memory profile much more predictable.

__Physics isn’t free.__  Unreal lets you set up physics — ragdolls and breakable objects etc — very easily. But physics is computationally expensive. You want simplified collision models or — even better — primitive colliders like cubes and spheres — whenever you can get away with them. Anything which talks to the physics simulation is also expensive: raycasts, sweep tests, and overlap events for example, This doesn’t mean you can’t do those, just use them as sparingly as you can.

__Don’t overdo content__ . Make sure that your models and textures are only as detailed as they need to be in game. A 4096x4096 texture is _not_  automatically “better” than a 512x512 — in fact, if the object you apply it to is never very large on screen it’s objectively worse, since you’ll see an auto-generate mipmap rather than the hand-created texture. More polygons don’t make things look ‘better’ unless they improve shading or silhouettes. Overly large textures and models suck up memory and graphics performance.

__Know your hardware.__  Unfortunately this requires some expert knowledge, but the takeaway is that not all platforms are created equal. Mobile hardware tends to really hate overdraw (ie, drawing many transparent polygons). PCs can have very different behavior depending on their graphics cards and memory footprint. Tricks that work on an Xbox don’t work as well on a PS and vice-versa.

Sorry this can only scratch the surface. Good luck, and maybe you should check out the [Unreal Slackers](http://unrealslackers.org/) Discord group.

