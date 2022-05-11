# What does it take to develop a graphics/animation intensive Android game or one can simply develop a game using only Java programming (is it possible)?

	author: Steve Theodore
	written: 2017-09-07
	views: 297
	upvotes: 0
	quora url: /What-does-it-take-to-develop-a-graphics-animation-intensive-Android-game-or-one-can-simply-develop-a-game-using-only-Java-programming-is-it-possible/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


It’s possible: after Minecraft is done in Java and it’s been _moderately_ successful.

OTOH there are plenty of alternative techs for doing games on Android. There is a lot of work involved in creating a really well rounded game engine — and doing it in Java, where there’s not a historically strong gaming/graphics ecosystem will mean doing a lot of that yourself. It’s probably easier to try one of the existing engines like [Unreal](https://docs.unrealengine.com/latest/INT/Platforms/Android/) (C++) or [Unity](https://docs.unity3d.com/Manual/android-GettingStarted.html) (C++ and C#): a lot of the most tedious and difficult work will already be done for you. A lot of the reason C++ is popular for game dev lies in the fact that C++ lets you get down and dirty with memory management — that’s a big advantage on slower, battery powered platforms and it’s hard to do in Java. It also allows you to avoid hitches caused by garbage collection, which can be easy to create by accident if you write a game the way you’d write a piece of conventional business software.

However, if you really love Java there’s [jMonkey](http://jmonkeyengine.org/), which is more or less a complete engine in the mold of Unity, and [LWJGL](https://www.lwjgl.org/)which is not really an engine but gives you a good starting point to make your own. If you’re not pushing the performance envelope too hard either of these would be doable.

